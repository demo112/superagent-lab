"""hello.py 的回归测试：用 subprocess 覆盖本单三条判据（含 stderr 与退出码 2）。"""

import subprocess
import sys
import unittest
from pathlib import Path

HELLO = Path(__file__).resolve().parent / "hello.py"


def run_hello(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, HELLO.name, *args],
        cwd=HELLO.parent,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )


class HelloTest(unittest.TestCase):
    def test_name_outputs_greeting(self) -> None:
        result = run_hello("--name", "观澜")

        self.assertEqual(result.stdout, "你好，观澜！\n")
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.returncode, 0)

    def test_no_args_keeps_original_output(self) -> None:
        result = run_hello()

        self.assertEqual(result.stdout, "你好，世界！\n")
        self.assertEqual(result.stderr, "")
        self.assertEqual(result.returncode, 0)

    def test_name_without_value_writes_usage_to_stderr(self) -> None:
        result = run_hello("--name")

        self.assertEqual(result.stdout, "")
        self.assertIn("usage", result.stderr.lower())
        self.assertIn("--name", result.stderr)
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()

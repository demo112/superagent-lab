"""hello.py 的单元测试：默认一行问候、--repeat N 打印 N 行。"""

import io
import unittest
from contextlib import redirect_stdout
from unittest import mock

import hello


def run_main(argv):
    """用给定命令行参数调用 hello.main()，返回它打印的每一行。"""
    stdout = io.StringIO()
    with mock.patch("sys.argv", ["hello.py", *argv]), redirect_stdout(stdout):
        hello.main()
    return stdout.getvalue().splitlines()


class HelloMainTest(unittest.TestCase):
    def test_default_prints_one_greeting_line(self):
        self.assertEqual(run_main([]), [hello.GREETING])

    def test_repeat_three_prints_three_greeting_lines(self):
        self.assertEqual(run_main(["--repeat", "3"]), [hello.GREETING] * 3)


if __name__ == "__main__":
    unittest.main()

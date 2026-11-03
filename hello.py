#!/usr/bin/env python3
"""打印中文问候，可用 --repeat 重复多行。"""

import argparse

GREETING = "你好，世界！"


def main() -> None:
    parser = argparse.ArgumentParser(description="打印中文问候")
    parser.add_argument(
        "--repeat",
        type=int,
        default=1,
        metavar="N",
        help="重复打印 N 行问候（默认 1 行）",
    )
    args = parser.parse_args()
    for _ in range(args.repeat):
        print(GREETING)


if __name__ == "__main__":
    main()

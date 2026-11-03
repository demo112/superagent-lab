import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="输出中文问候。")
    parser.add_argument("--name", metavar="名字", help="要问候的名字")
    args = parser.parse_args()

    if args.name:
        print(f"你好，{args.name}！")
    else:
        print("你好，世界！")


if __name__ == "__main__":
    main()

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="输出中文问候。")
    parser.add_argument("name", nargs="?", metavar="名字", help="要问候的名字")
    parser.add_argument("--name", dest="name_option", metavar="名字", help="要问候的名字")
    args = parser.parse_args()

    name = args.name_option if args.name_option is not None else args.name
    if name:
        print(f"你好，{name}！")
    else:
        print("你好，世界！")


if __name__ == "__main__":
    main()

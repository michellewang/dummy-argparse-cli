import argparse

DEFAULT_NAME = "world"


def get_parser():
    parser = argparse.ArgumentParser(description="A dummy CLI tool for testing.")
    parser.add_argument("--name", type=str, help="Input file", default=DEFAULT_NAME)
    return parser


def print_name(name: str = DEFAULT_NAME):
    print(f"Hello, {name}!")


def main():
    parser = get_parser()
    args = parser.parse_args()
    print_name(args.name)


if __name__ == "__main__":
    main()

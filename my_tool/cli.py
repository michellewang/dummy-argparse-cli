import argparse

DEFAULT_NAME = "world"


def get_parser():
    parser = argparse.ArgumentParser(description="A dummy CLI tool for testing.")
    parser.add_argument("--name", type=str, help="Input file", default=DEFAULT_NAME)
    parser.add_argument(
        "--bye", action="store_true", help="Whether to say goodbye instead of hello."
    )
    return parser


def print_name(name: str = DEFAULT_NAME, bye: bool = False):
    if not bye:
        prefix = "Hello"
    else:
        prefix = "Goodbye"
    print(f"{prefix}, {name}!")


def main():
    parser = get_parser()
    args = parser.parse_args()
    print_name(args.name, bye=args.bye)


if __name__ == "__main__":
    main()

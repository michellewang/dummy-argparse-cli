import click

DEFAULT_NAME = "world"


def print_name(name: str = DEFAULT_NAME, bye: bool = False):
    if not bye:
        prefix = "Hello"
    else:
        prefix = "Goodbye"
    print(f"{prefix}, {name}!")


@click.group()
def group():
    pass


@group.command()
def version():
    click.echo("dummy-cli-click-group 1.0")


@group.command()
@click.option("--name", default=DEFAULT_NAME, help="Input file")
@click.option("--bye", is_flag=True, help="Whether to say goodbye instead of hello.")
def greet(name, bye):
    print_name(name, bye=bye)


if __name__ == "__main__":
    group()

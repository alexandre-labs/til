import datetime
import sys

import click


@click.command()
@click.argument('title')
def til(title):

    click.clear()
    banner = f"Today I learned: {title}\n"
    click.echo("-" * len(banner))
    click.echo(banner)

    click.echo("Description: \n\n")

    description = ""
    for line in sys.stdin:
        description += line
        if line.strip() == "TIL!":
            break

    click.echo(f"{banner} - {datetime.date.today()}")


if __name__ == "__main__":
    til()

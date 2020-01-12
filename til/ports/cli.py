import datetime
import pathlib
import sys

import click
import git
from dynaconf import settings


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


@click.command('repo-init')
@click.argument('repo-name')
def repo_init(repo_name):

    # TODO: implement a better map between name and repo
    if repo_name == 'local':

        til_data_path = pathlib.Path(settings.REPOSITORIES.LOCAL.DATA_PATH)

        if not til_data_path.is_dir():
            # Read and write for the owner; only read for everybody else
            til_data_path.mkdir(parents=True)

        git.Repo.init(til_data_path)

        click.echo("Local repository initialized successfully")


@click.group()
def manage():
    pass


manage.add_command(repo_init)

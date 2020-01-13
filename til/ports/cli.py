import datetime
import pathlib
import sys

import click
import git
from dynaconf import settings

from til.application.usecases.register_a_til import RegisterTILRequest, RegisterTIL
from til.infrastructure.repositories.local.learning import LearningRepository


@click.command()
@click.argument('title')
def til(title):

    banner = f"Today I learned: {title}\n"
    banner += "-" * len(banner)
    click.echo(banner)

    click.echo("\nDescription: \n")

    description = f"{banner}\n"
    for line in sys.stdin:
        description += line
        if line.strip() == "TIL!":
            description += "\n"
            break

    uc = RegisterTIL(
        settings=settings,
        repository=LearningRepository(settings=settings)
    )

    request = RegisterTILRequest.create(
        title, description, timestamp=datetime.datetime.now()
    )

    result = uc.execute(request=request)

    if result:
        click.echo("Done!")
        click.echo(result.result)
    else:
        click.echo("Error: ")
        click.echo(result.result)
        click.Abort()


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

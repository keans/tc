import click

from .cmds import start_project, stop_project, status_project, \
    list_projects, cancel_project, export_projects


@click.group()
def cli():
    pass


def validate_tags(ctx, param, value):
    try:
        tags = []
        for tag in value:
            if tag.startswith("+"):
                tags.append(tag[1:])
            else:
                raise ValueError
        return tags
    except ValueError:
        raise click.BadParameter("The tags must start with '+'.")


@cli.command(
    help="start a new running project"
)
@click.argument("project")
@click.argument("tags", nargs=-1, callback=validate_tags)
@click.option("--description")
def start(project, tags, description):
    start_project(project, tags, description)


@cli.command(
    help="stop the currently running project"
)
def stop():
    stop_project()


@cli.command(
    help="show the status of the currently running project"
)
def status():
    status_project()


@cli.command(
    help="cancel currently running project"
)
def cancel():
    cancel_project()


@cli.command(
    help="list all available projects"
)
def list():
    list_projects()


@cli.command(
    help="export all available projects"
)
@click.option('--type', type=click.Choice(["csv"]), default="csv")
@click.argument("output", type=click.File("w"))
def export(output, type):
    export_projects(output, type)

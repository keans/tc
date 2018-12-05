import click

from .cmds import start_project, stop_project, status_project, \
    list_projects, cancel_project, export_projects, remove_project
from .paramtypes import DateTimeType


@click.group()
def cli():
    pass


def validate_tags(ctx, param, value):
    """
    helper to check tags input arguments
    """
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
    help="Start a new running project."
)
@click.argument("project")
@click.argument("tags", nargs=-1, callback=validate_tags)
@click.option(
    "--description",
    help="Additional description for the project."
)
def start(project, tags, description):
    start_project(project, tags, description)


@cli.command(
    help="Stop the currently running project."
)
@click.option(
    "--at", default="", type=DateTimeType(),
    help="Stop time (after start time, but not in the future)."
)
def stop(at):
    stop_project(at)


@cli.command(
    help="Show the status of the currently running project."
)
def status():
    status_project()


@cli.command(
    help="Cancel currently running project."
)
def cancel():
    cancel_project()


@cli.command(
    help="Remove project with given uuid."
)
@click.argument("project_uuid")
def remove(project_uuid):
    remove_project(project_uuid)


@cli.command(
    help="List all available projects."
)
def list():
    list_projects()


@cli.command(
    help="Export all available projects."
)
@click.option(
    "--type", type=click.Choice(["csv"]), default="csv", show_default=True,
    help="Type of export that is used."
)
@click.argument("output", type=click.File("w"))
def export(output, type):
    export_projects(output, type)

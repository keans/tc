import datetime

import click

from .cmds import start_project, stop_project, status_project, \
    list_projects, cancel_project, export_projects, remove_project, \
    list_tags, project_logs
from .paramtypes import DateTimeType, TagType


@click.group(
    help="Simple time tracker."
)
def cli():
    pass


@cli.command(
    help="Start a new running project."
)
@click.argument("project")
@click.argument("tags", nargs=-1, type=TagType())
@click.option(
    "--description",
    help="Additional description for the project."
)
@click.option(
    "--at", default="", type=DateTimeType(),
    help="Start time (if not provided current time is used)."
)
def start(at, project, tags, description):
    start_project(at, project, tags, description)


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
@click.argument("project_uuid", type=str, default=-1)
def status(project_uuid):
    status_project(project_uuid)


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
    help="List all logged projects in detail."
)
@click.option(
    "--from-date", type=DateTimeType(),
    default=datetime.datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    ),
    help="From date"
)
@click.option(
    "--to-date", type=DateTimeType(), default=datetime.datetime.now(),
    help="To date"
)
@click.option(
    "--project", type=str, default=None,
    help="Project name."
)
@click.option(
    "--tag", type=TagType(), default=None,
    help="Tag name."
)
def log(from_date, to_date, project, tag):
    project_logs(from_date, to_date, project, tag, False)


@cli.command(
    help="List all logged projects in short form."
)
@click.option(
    "--from-date", type=DateTimeType(),
    default=datetime.datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    ),
    help="From date"
)
@click.option(
    "--to-date", type=DateTimeType(), default=datetime.datetime.now(),
    help="To date"
)
@click.option(
    "--project", type=str, default=None,
    help="Project name."
)
@click.option(
    "--tag", type=TagType(), default=None,
    help="Tag name."
)
def shortlog(from_date, to_date, project, tag):
    project_logs(from_date, to_date, project, tag, True)


@cli.command(
    help="List all available projects."
)
def projects():
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


@cli.command(
    help="List all tags."
)
def tags():
    list_tags()

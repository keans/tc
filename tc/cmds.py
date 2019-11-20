import datetime
import collections

import click

from .utils import format_timedelta, format_project, format_project_detail
from .projectmanager import ProjectManager
from .project import Project


def start_project(at, project, tags, description):
    """
    start new project and mark it as current
    """
    if at is not None and at > datetime.datetime.now():
        # ensure start date is not in the future
        click.echo("The start time cannot be in the future.")
        raise click.Abort()

    pm = ProjectManager()
    if pm.has_current_project:
        # existing project running => abort
        click.echo("There is already a running project.")
        raise click.Abort()

    # start new project
    p = Project(
        uuid=pm._get_unique_uuid(), name=project,
        tags=tags, description=description
    )

    p.start(at)
    pm.save_current(p)

    click.echo(
        "Starting project '{}' at {}.".format(
            p.name, p.start_time.strftime("%H:%M")
        )
    )


def stop_project(at):
    """
    stops the currently running project
    """
    pm = ProjectManager()
    if not pm.has_current_project:
        click.echo("There is no running project.")
        raise click.Abort()

    # get current project
    current_project = pm.get_current()
    if at is not None:
        if at < current_project.start_time:
            click.echo("The stop time cannot be before the start time.")
            raise click.Abort()
        elif at > datetime.datetime.now():
            click.echo("The stop time cannot be in the future.")
            raise click.Abort()

    # stop project at given time and remove it from running
    current_project.stop(at)
    pm.cancel_current()

    # store current project in projects list
    pm.add_project(current_project)
    pm.save()

    click.echo(
        "Stopped project '{}' at {} (duration: {}).".format(
            current_project.name,
            current_project.end_time.strftime("%H:%M:%S"),
            format_timedelta(current_project.duration)
        )
    )


def status_project(project_uuid):
    """
    shows the status of the current project
    """
    pm = ProjectManager()

    p = None
    if project_uuid != -1:
        # get selected project
        p = pm.get_project(project_uuid)
        if p is None:
            click.echo("There is no project '{}'.".format(project_uuid))
            raise click.Abort()

    else:
        # get current project
        p = pm.get_current()
        if not pm.has_current_project:
            click.echo("There is no running project.")
            raise click.Abort()

    click.echo(format_project(p))


def cancel_project():
    """
    cancel the current project
    """
    pm = ProjectManager()
    if not pm.has_current_project:
        click.echo("There is no running project.")
        raise click.Abort()
    p = pm.get_current()
    pm.cancel_current()

    click.echo(
        "Canceled currently running project '{}'.".format(
            p.name
        )
    )


def project_logs(from_date, to_date, project, tag, short_format):
    """
    show a tracked projects in short form
    """
    pm = ProjectManager()
    for p in pm.projects:
        if (p.start_time >= from_date) and (p.end_time <= to_date):
            if (project is not None) and (p.name != project):
                # skip projects that do not have selected name
                continue

            if (tag is not None) and (tag not in p.tags):
                # skip projects that do not have selected tag
                continue

            if short_format is True:
                click.echo(format_project(p))
            else:
                click.echo(format_project_detail(p))


def remove_project(project_uuid):
    """
    remove project with given uuid
    """
    pm = ProjectManager()
    res = pm.remove_project(project_uuid)
    if res is True:
        click.echo("Removed project '{}'.".format(project_uuid))
        pm.save()
    else:
        click.echo("There is no project '{}'.".format(project_uuid))
        raise click.Abort()


def export_projects(output, type_):
    """
    export
    """
    pm = ProjectManager()
    if type_ == "csv":
        pm.csv_export(output)


def list_projects():
    """
    show a list of all projects
    """
    pm = ProjectManager()

    # count projects
    c = collections.Counter()
    for p in pm.projects:
        c[p.name] += 1

    for tag, count in c.items():
        print("{:4}  {}".format(count, tag))


def list_tags():
    """
    show a list of all tags
    """
    pm = ProjectManager()

    # count tags
    c = collections.Counter()
    for p in pm.projects:
        for tag in p.tags:
            c[tag] += 1

    for tag, count in c.items():
        print("{:4}  {}".format(count, tag))

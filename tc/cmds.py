import click

from .utils import format_timedelta
from .projectmanager import ProjectManager
from .project import Project


def start_project(project, tags, description):
    """
    start new project and mark it as current
    """
    pm = ProjectManager()
    if pm.has_current_project:
        click.echo("There is already a running project.")
        raise click.Abort()

    # start new project
    p = Project(name=project, tags=tags, description=description)
    p.start()
    pm.save_current(p)

    click.echo(
        "Starting project '{}' at {}.".format(
            p.name, p.start_time.strftime("%H:%M")
        )
    )


def stop_project():
    """
    stops the currently running project
    """
    pm = ProjectManager()
    if not pm.has_current_project:
        click.echo("There is no running project.")
        raise click.Abort()

    # get current project
    current_project = pm.get_current(remove=True)
    current_project.stop()

    # store current project in projects list
    pm.add_project(current_project)
    pm.save()

    click.echo(
        "Stopped project '{}' at {} (duration: {}).".format(
            current_project.name,
            current_project.end_time.strftime("%H:%M:%S"),
            current_project.duration
        )
    )


def status_project():
    """
    shows the status of the current project
    """
    pm = ProjectManager()
    if not pm.has_current_project:
        click.echo("There is no running project.")
    else:
        p = pm.get_current()
        click.echo(
            "{}".format(
                p.name
            )
        )


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


def list_projects():
    """
    show a list of all completed
    """
    pm = ProjectManager()
    for p in pm.projects:
        click.echo(
            "{:10} {} to {}  {:>8}  {:15} {}".format(
                p.uuid,
                p.start_time.strftime("%H:%M"),
                p.end_time.strftime("%H:%M"),
                format_timedelta(p.duration),
                p.name,
                "[{}]".format(",".join(p.tags))
                if len(p.tags) > 0
                else ""
            )
        )


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

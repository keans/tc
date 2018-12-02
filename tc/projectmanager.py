import os
import json
import csv

from .config import CURRENT_PROJECT, PROJECTS
from .project import Project


class ProjectManager:
    def __init__(self, auto_load=True):
        self.projects = []

        if auto_load is True:
            self.load()

    def save(self, indent=4):
        """
        save all projects to file
        """
        with open(PROJECTS, "w") as f:
            d = {
                "projects": [
                    p.dict()
                    for p in self.projects
                ]
            }
            json.dump(d, f, indent=indent)

    def load(self):
        """
        load all projects from file
        """
        if os.path.exists(PROJECTS):
            with open(PROJECTS, "r") as f:
                j = json.load(f)
                self.projects = [
                    Project.create_from_dict(d)
                    for d in j["projects"]
                ]

    @property
    def has_current_project(self):
        return os.path.exists(CURRENT_PROJECT)

    def cancel_current(self):
        """
        cancel the current project by simply deleting it
        """
        if os.path.exists(CURRENT_PROJECT):
            os.remove(CURRENT_PROJECT)

    def get_current(self, remove=False):
        """
        get current project from stored file
        """
        if not os.path.exists(CURRENT_PROJECT):
            # file is not existing
            return None

        p = None
        with open(CURRENT_PROJECT, "r") as f:
            p = Project.create_from_dict(json.load(f))

        if remove is True:
            # remove current project file
            os.remove(CURRENT_PROJECT)

        return p

    def save_current(self, project):
        """
        save the project as current
        """
        with open(CURRENT_PROJECT, "w") as f:
            json.dump(project.dict(), f)

    def add_project(self, project):
        """
        add project to the list of projects
        """
        self.projects.append(project)

    def csv_export(self, f):
        fieldnames = [
            "uuid", "name", "start_time", "end_time",
            "description", "tags"
        ]
        writer = csv.DictWriter(f, fieldnames)
        writer.writeheader()
        for p in self.projects:
            writer.writerow(p.dict())

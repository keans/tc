import uuid
import datetime

import dateutil.parser


class Project:
    """
    class that represents a project
    """
    def __init__(
        self, name="", start_time="", end_time="", description="", tags=[]
    ):
        self.uuid = str(uuid.uuid4())[:8]
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.tags = tags

    @classmethod
    def create_from_dict(cls, d):
        """
        create a Project class instance from the given dictionary
        """
        p = Project()
        p.parse(d)

        return p

    @property
    def duration(self):
        """
        returns the duration of the project
        """
        if self.end_time == "":
            return None

        return self.end_time - self.start_time

    def start(self):
        """
        set the start time to the current time
        """
        self.start_time = datetime.datetime.now()

    def stop(self):
        """
        set the stop time to the current time
        """
        self.end_time = datetime.datetime.now()

    def parse(self, j):
        """
        parse given dictionary and put variables in the
        internal variables
        """

        self.uuid = j["uuid"]
        self.name = j["name"]
        self.start_time = (
            dateutil.parser.parse(j["start_time"])
            if j["start_time"] not in ("", None)
            else None
        )
        self.end_time = (
            dateutil.parser.parse(j["end_time"])
            if j["end_time"] not in ("", None)
            else None
        )
        self.description = j["description"]
        self.tags = j["tags"]

    def dict(self):
        """
        returns the inner variables as dictionary
        """
        return {
            "uuid": self.uuid,
            "name": self.name,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else "",
            "description": self.description,
            "tags": self.tags,
        }

    def __str__(self):
        return "<Project(uuid='{}', name='{}', start='{}', end='{}', " \
               "description='{}', tags={})>".format(
                    self.uuid,
                    self.name,
                    self.start_time,
                    self.end_time,
                    self.description,
                    self.tags
                )

import uuid
import datetime


class Project:
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
        self.start_time = datetime.datetime.now()

    def stop(self):
        self.end_time = datetime.datetime.now()

    def parse(self, j):
        self.uuid = j["uuid"]
        self.name = j["name"]
        self.start_time = (
            datetime.datetime.fromisoformat(j["start_time"])
            if j["start_time"] != ""
            else None
        )
        self.end_time = (
            datetime.datetime.fromisoformat(j["end_time"])
            if j["end_time"] != ""
            else None
        )
        self.description = j["description"]
        self.tags = j["tags"]

    def dict(self):
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

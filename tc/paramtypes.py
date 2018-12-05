import datetime

import click
from dateutil.parser import parse


class DateTimeType(click.ParamType):
    """
    parses date
    """

    name = "DATE_TIME"

    def convert(self, value, param, ctx):
        try:
            if value == "":
                return None

            if isinstance(value, datetime.datetime):
                return value

            return parse(value)

        except ValueError:
            self.fail(
                "'{}'' is not a support time format".format(value)
            )


class TagType(click.ParamType):
    """
    parses tag
    """

    name = "TAG"

    def convert(self, value, param, ctx):
        if not value.startswith("+"):
            self.fail(
                "A tag must start with '+'."
            )

        return value[1:]

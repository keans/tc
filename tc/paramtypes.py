from dateutil.parser import parse

import click


class DateTimeType(click.ParamType):
    """
    parses date
    """

    name = "DATE_TIME"

    def convert(self, value, param, ctx):
        try:
            if value == "":
                return None

            return parse(value)
        except ValueError:
            self.fail(
                "'{}'' is not a support time format".format(value)
            )

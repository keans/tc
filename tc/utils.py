
def format_timedelta(tdelta):
    """
    pretty output for timedelta
    """
    d = dict(days=tdelta.days)
    d["hrs"], rem = divmod(tdelta.seconds, 3600)
    d["min"], d["sec"] = divmod(rem, 60)

    if d["min"] is 0:
        fmt = "{sec}s"
    elif d["hrs"] is 0:
        fmt = "{min}m{sec}s"
    elif d["days"] is 0:
        fmt = "{hrs}h{min}m{sec}s"
    else:
        fmt = "{days}d{hrs}h{min}m{sec}s"

    return fmt.format(**d)


def format_project(p):
    return "{:10} {:5} to {:5}  {:>8}  {:15} {}".format(
        p.uuid,
        p.start_time.strftime("%H:%M"),
        p.end_time.strftime("%H:%M") if p.end_time != None else "*running*",
        format_timedelta(p.duration),
        p.name,
        "[{}]".format(",".join(p.tags))
        if len(p.tags) > 0 else "",
    )


def format_project_detail(p):
    return "        uuid:  {}\n     project:  {}\n        from:  {}\n" \
           "          to:  {}\n    duration:  {}{}\n{}".format(
                p.uuid,
                p.name,
                p.start_time.strftime("%a, %d %b %Y %H:%M"),
                p.end_time.strftime("%a, %d %b %Y %H:%M")
                if p.end_time is not None else "*running*",
                format_timedelta(p.duration),
                "\n        tags:  [{}]".format(",".join(p.tags))
                if len(p.tags) > 0 else "",
                " description:  {}\n".format(p.description)
                if p.description else ""
            )

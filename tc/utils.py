
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

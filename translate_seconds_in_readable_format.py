def format_duration(seconds):
    if seconds == 0:
        return "now"

    # seconds = seconds % (24 * 3600)
    # hour = seconds // 3600
    # seconds %= 3600
    # minutes = seconds // 60
    # seconds %= 60
    # day = hour // 24
    # year = day // 365

    time_parts = []
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    # Helper function to format plural units (second or seconds, etc.)
    def plural(value, unit):
        if value == 1:
            return f"{value} {unit}"
        elif value > 1:
            return f"{value} {unit}s"
        return None

    # Create a list of formatted time parts
    for value, unit in [(years, "year"), (days, "day"), (hours, "hour"), (minutes, "minute"), (seconds, "second")]:
        part = plural(value, unit)
        if part:
            time_parts.append(part)

    # Join the parts with commas and 'and'
    if len(time_parts) == 1:
        return time_parts[0]
    else:
        return ', '.join(time_parts[:-1]) + " and " + time_parts[-1]
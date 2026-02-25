from datetime import datetime, timedelta, timezone
import re
import sys

def parse_datetime_with_tz(line):
    """
    Parse string like:  YYYY-MM-DD HH:MM:SS UTC±HH:MM
    Return datetime object in the specified timezone (local time).
    """
    pattern = r'^(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2}):(\d{2})\s+UTC([+-])(\d{2}):(\d{2})$'
    m = re.match(pattern, line.strip())
    if not m:
        sys.exit("Invalid datetime format")

    year   = int(m.group(1))
    month  = int(m.group(2))
    day    = int(m.group(3))
    hour   = int(m.group(4))
    minute = int(m.group(5))
    second = int(m.group(6))

    sign   = 1 if m.group(7) == '+' else -1
    off_h  = int(m.group(8))
    off_m  = int(m.group(9))

    offset_sec = sign * (off_h * 3600 + off_m * 60)
    tz = timezone(timedelta(seconds=offset_sec))

    return datetime(year, month, day, hour, minute, second, tzinfo=tz)


def main():
    start_str = input().strip()
    end_str   = input().strip()

    start_local = parse_datetime_with_tz(start_str)
    end_local   = parse_datetime_with_tz(end_str)

    # Convert both moments to UTC
    start_utc = start_local.astimezone(timezone.utc)
    end_utc   = end_local.astimezone(timezone.utc)

    # Duration in seconds
    duration_sec = int((end_utc - start_utc).total_seconds())

    print(duration_sec)


if __name__ == "__main__":
    main()
from datetime import datetime, timedelta, timezone
import re
import sys

def parse_date_with_tz(line):
    # Format: YYYY-MM-DD UTC±HH:MM
    pattern = r'^(\d{4})-(\d{2})-(\d{2})\s+UTC([+-])(\d{2}):(\d{2})$'
    m = re.match(pattern, line.strip())
    if not m:
        sys.exit("Invalid input format")
    
    year  = int(m.group(1))
    month = int(m.group(2))
    day   = int(m.group(3))
    sign  = 1 if m.group(4) == '+' else -1
    h     = int(m.group(5))
    m     = int(m.group(6))
    
    offset_seconds = sign * (h * 3600 + m * 60)
    tz = timezone(timedelta(seconds=offset_seconds))
    
    # Local midnight = 00:00:00 in the given time zone
    return datetime(year, month, day, 0, 0, 0, tzinfo=tz)

def is_leap_year(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def get_next_birthday(birth_local, curr_utc):
    b_month = birth_local.month
    b_day   = birth_local.day
    curr_year = curr_utc.year
    
    # Try current year first
    candidates = []
    
    for year in range(curr_year, curr_year + 3):
        day = b_day
        if b_month == 2 and b_day == 29 and not is_leap_year(year):
            day = 28
        
        try:
            cand_local = datetime(year, b_month, day, 0, 0, 0, tzinfo=birth_local.tzinfo)
        except ValueError:
            # shouldn't happen after Feb 29 adjustment
            continue
        
        # Convert candidate to UTC
        cand_utc = cand_local.astimezone(timezone.utc)
        
        # We want candidates >= current moment
        if cand_utc >= curr_utc:
            candidates.append(cand_utc)
    
    if not candidates:
        # Very unlikely (would need broken logic)
        return 0
    
    # Nearest = earliest among future ones
    next_bday_utc = min(candidates)
    
    # Difference in seconds
    delta_sec = (next_bday_utc - curr_utc).total_seconds()
    
    # Round to nearest integer day (as per problem: days left)
    # Problem wants floor((seconds + 86399) // 86400) ? No:
    # From examples → exact midnight-to-midnight difference in days
    days = round(delta_sec / 86400)
    
    return int(days)

def main():
    birth_str = input().strip()
    curr_str  = input().strip()
    
    birth_local = parse_date_with_tz(birth_str)
    curr_local  = parse_date_with_tz(curr_str)
    
    # Convert both to UTC for easy comparison
    curr_utc = curr_local.astimezone(timezone.utc)
    
    days_left = get_next_birthday(birth_local, curr_utc)
    
    print(days_left)

if __name__ == "__main__":
    main()
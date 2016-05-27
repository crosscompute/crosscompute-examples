from dateutil.parser import parse as parse_timestamp
from math import ceil
from sys import argv


a_timestamp, b_timestamp = map(parse_timestamp, argv[1:])
second_count = (b_timestamp - a_timestamp).total_seconds()
minute_count = second_count / 60.
hour_count = minute_count / 60.
day_count = hour_count / 24.


if day_count > 1:
    print('day_count = %s' % int(ceil(day_count)))
elif hour_count > 1:
    print('hour_count = %s' % int(ceil(hour_count)))
elif minute_count > 1:
    print('minute_count = %s' % int(ceil(minute_count)))
else:
    print('second_count = %s' % int(ceil(second_count)))

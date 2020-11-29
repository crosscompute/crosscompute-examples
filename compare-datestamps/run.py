import json
import sys
from datetime import datetime
from math import ceil
from os.path import join


def parse_datestamp(datestamp):
    return datetime.strptime(datestamp, '%Y%m%d')


def estimate_time_difference(source_datestamp, target_datestamp):
    second_count = (target_datestamp - source_datestamp).total_seconds()
    minute_count = second_count / 60.
    hour_count = minute_count / 60.
    day_count = hour_count / 24.
    week_count = day_count / 7.
    month_count = week_count / 4.34524
    year_count = month_count / 12.

    if year_count > 1:
        count = int(ceil(year_count))
        unit = 'year' if count == 1 else 'years'
    elif month_count > 1:
        count = int(ceil(month_count))
        unit = 'month' if count == 1 else 'months'
    elif week_count > 1:
        count = int(ceil(week_count))
        unit = 'week' if count == 1 else 'weeks'
    else:
        count = int(ceil(day_count))
        unit = 'day' if count == 1 else 'days'

    return {'count': count, 'unit': unit}


def log_and_exit(error_dictionary, folder):
    json.dump(error_dictionary, open(join(folder, 'variables.json'), 'wt'))
    sys.exit(error_dictionary)


if __name__ == '__main__':
    input_folder, output_folder, log_folder, debug_folder = sys.argv[1:]
    input_dictionary = json.load(open(join(
        input_folder, 'variables.json'), 'rt'))
    d = {}
    for key in 'source_datestamp', 'target_datestamp':
        try:
            d[key] = parse_datestamp(input_dictionary[key])
        except ValueError:
            log_and_exit({key: 'could not parse date'}, log_folder)
    output_dictionary = estimate_time_difference(
        d['source_datestamp'], d['target_datestamp'])
    json.dump(output_dictionary, open(join(
        output_folder, 'variables.json'), 'wt'))

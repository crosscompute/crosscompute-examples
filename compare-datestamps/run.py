import json
import sys
from datetime import datetime
from math import ceil
from os.path import join


def parse_datestamp(datestamp):
    return datetime.strptime(datestamp, '%Y%m%d')


def log_and_exit(error_dictionary, folder):
    json.dump(error_dictionary, open(join(folder, 'variables.json'), 'wt'))
    sys.exit(error_dictionary)


def estimate_time_difference(source_date, target_date):
    second_count = (target_date - source_date).total_seconds()
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


def render_description(variable_dictionary, output_dictionary):
    source_date = variable_dictionary['source_date']
    target_date = variable_dictionary['target_date']
    count = output_dictionary['count']
    unit = output_dictionary['unit']

    FRIENDLY_FORMAT = '%A, %B %d, %Y'
    source_string = source_date.strftime(FRIENDLY_FORMAT)
    target_string = target_date.strftime(FRIENDLY_FORMAT)

    preposition = 'after' if source_date > target_date else 'before'
    return (
        f'{source_string} is approximately '
        f'**{count} {unit} {preposition}** {target_string}.')


if __name__ == '__main__':
    input_folder, output_folder, log_folder, debug_folder = sys.argv[1:]
    input_dictionary = json.load(open(join(
        input_folder, 'variables.json'), 'rt'))
    d = {}
    for key in 'source_datestamp', 'target_datestamp':
        try:
            value = parse_datestamp(input_dictionary[key])
        except ValueError:
            log_and_exit({key: 'could not parse date'}, log_folder)
        d[key.replace('stamp', '')] = value
    output_dictionary = estimate_time_difference(
        d['source_date'], d['target_date'])
    json.dump(output_dictionary, open(join(
        output_folder, 'variables.json'), 'wt'))

    open(join(output_folder, 'description.md'), 'wt').write(
        render_description(d, output_dictionary))

import json
import pendulum
from os.path import join
from pandas import read_csv
from sys import argv


input_folder, output_folder, log_folder, debug_folder = argv[1:]
table = read_csv(join(input_folder, 'table.csv'))
settings = json.load(open(join(input_folder, 'settings.json'), 'rt'))
timestamp_format = settings['timestamp_format']


old_column_names = table.columns
for old_column_name in old_column_names:
    values = []
    for raw_value in table[old_column_name]:
        try:
            value = pendulum.parse(raw_value)
        except (pendulum.exceptions.ParserError, TypeError):
            value = ''
        if value != '':
            value = value.format(timestamp_format)
        values.append(value)
    if len(set(values).difference([''])) == 0:
        continue
    index = 2
    new_column_name = old_column_name + ' ' + str(index)
    while new_column_name in old_column_names:
        index += 1
        new_column_name = old_column_name + ' ' + str(index)
    table[new_column_name] = values
table.to_csv(join(output_folder, 'table.csv'), index=False)

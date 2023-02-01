import csv
import fcntl
import json
from os.path import exists, join
from pathlib import Path
from sys import argv


input_folder, output_folder = argv[1:]
variables = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))


datasets_folder = Path('datasets')
datasets_folder.mkdir(exist_ok=True)
table_path = datasets_folder / 'entries.csv'
is_table_new = True
is_entry_new = True


if exists(table_path):
    key = 'repository_url'
    repository_url = variables[key].strip()
    with open(table_path, 'rt') as f:
        csv_reader = csv.reader(f)
        columns = next(csv_reader)
        column_index = columns.index(key)
        for row in csv_reader:
            if row[column_index] == repository_url:
                is_entry_new = False
    is_table_new = False


with open(table_path, 'at') as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    csv_writer = csv.writer(f)
    if is_table_new:
        csv_writer.writerow(variables.keys())
    csv_writer.writerow(variables.values())


if is_entry_new:
    response_text = 'Thanks for submitting a new entry!'
else:
    response_text = 'This entry already exists. Thanks for updating it!'
json.dump({
    'response_text': response_text,
}, open(join(output_folder, 'variables.dictionary'), 'wt'))

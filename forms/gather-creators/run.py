import csv
import fcntl
import json
from os.path import exists, join
from pathlib import Path
from sys import argv


input_folder, output_folder = argv[1:]
variables = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))


datasets_folder = Path('datasets')
table_path = datasets_folder / 'entries.csv'
is_new = not exists(table_path)
with open(table_path, 'at') as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    csv_writer = csv.writer(f)
    if is_new:
        csv_writer.writerow(variables.keys())
    csv_writer.writerow(variables.values())

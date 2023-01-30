import json
from collections import defaultdict
from datetime import datetime
from os import getenv
from pathlib import Path


input_folder = Path(getenv(
    'CROSSCOMPUTE_INPUT_FOLDER', 'batches/standard/input'))
output_folder = Path(getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'batches/standard/output'))


with (input_folder / 'variables.dictionary').open('rt') as f:
    d = json.load(f)
project_id = d['project_id']


def get_pomodoros_by_project_id(runs_folder):
    # TODO: Match identity
    pomodoros_by_project_id = defaultdict(list)
    for path in runs_folder.glob('**/input/variables.dictionary'):
        with path.open('rt') as f:
            d = json.load(f)
        project_id = d['project_id']
        pomodoro_datetime = datetime.fromtimestamp(path.stat().st_mtime)
        pomodoros_by_project_id[project_id].append({
            'datetime': pomodoro_datetime})
    return pomodoros_by_project_id


count_by_project_id = {}
runs_folder = Path('runs')
pomodoros_by_project_id = get_pomodoros_by_project_id(runs_folder)
project_ids = pomodoros_by_project_id.keys()
this_datetime = datetime.now()
this_date = this_datetime.date()
for project_id in project_ids:
    selected_pomodoros = []
    for pomodoro in pomodoros_by_project_id.get(project_id, []):
        if pomodoro['datetime'].date() == this_date:
            selected_pomodoros.append(pomodoro)
    count_by_project_id[project_id] = len(selected_pomodoros)
link_text = f'''
<a href="/a/log-pomodoro?project_id={project_id}">Log another pomodoro</a>.
'''.strip()


with (output_folder / 'counts.json').open('wt') as f:
    json.dump({
        'data': list(count_by_project_id.items()),
        'columns': ['project_id', 'count'],
    }, f)
with (output_folder / 'link.md').open('wt') as f:
    f.write(link_text)

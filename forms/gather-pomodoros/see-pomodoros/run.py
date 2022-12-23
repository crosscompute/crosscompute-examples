import json
from collections import defaultdict
from datetime import datetime
from os import getenv
from pathlib import Path


def get_pomodoros_by_project_id_by_date_by_username(runs_folder):
    d = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    for path in runs_folder.glob('**/input/variables.dictionary'):
        debug_folder = path.parents[1] / 'debug'
        with (debug_folder / 'identities.dictionary').open('rt') as f:
            identities = json.load(f)
        username = identities['username']
        pomodoro_datetime = datetime.fromtimestamp(path.stat().st_mtime)
        pomodoro_date = pomodoro_datetime.date()
        with path.open('rt') as f:
            variables = json.load(f)
        project_id = variables['project_id']
        d[username][pomodoro_date][project_id].append({
            'datetime': pomodoro_datetime})
    return d


output_folder = Path(getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'batches/standard/output'))
runs_folder = Path('datasets/runs')
summary_lines = []
for [
    username,
    pomodoros_by_project_id_by_date,
] in get_pomodoros_by_project_id_by_date_by_username(runs_folder).items():
    summary_lines.append('## ' + username)
    for [
        date,
        pomodoros_by_project_id,
    ] in sorted(
        pomodoros_by_project_id_by_date.items(),
        key=lambda _: _[0],
        reverse=True,
    ):
        summary_lines.append('### ' + date.strftime('%A, %B %d, %Y'))
        for [
            project_id,
            pomodoros,
        ] in pomodoros_by_project_id.items():
            summary_lines.append(f'- {project_id}: {len(pomodoros)} pomodoros')
with (output_folder / 'summary.md').open('wt') as f:
    f.write('\n'.join(summary_lines))

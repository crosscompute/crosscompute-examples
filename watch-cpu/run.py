import json
import psutil


def plot(output_folder):
    with open(output_folder / 'variables.dictionary', 'wt') as f:
        json.dump({'cpu_usage': psutil.cpu_percent(interval=1)}, f)

import json
import psutil


def plot(output_folder):
    with open(output_folder / 'variables.dictionary', 'wt') as f:
        json.dump({'ram_usage': psutil.virtual_memory().percent}, f)

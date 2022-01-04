import json
import psutil
from os.path import join


def plot(input_folder, output_folder):
    json.dump({
        'cpu-usage': psutil.cpu_percent(),
    }, open(join(output_folder, 'variables.dictionary'), 'wt'))

import csv
from time import time

import matplotlib.pyplot as plt
import psutil


def plot(log_folder, output_folder):
    unix_time = time()
    cpu_percent = psutil.cpu_percent(interval=1)

    with open(log_folder / 'cpu-usage.csv', 'a+t') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([unix_time, cpu_percent])
        csv_file.seek(0)
        csv_reader = csv.reader(csv_file)
        xs, ys = zip(*csv_reader)
        xs = [float(_) for _ in xs]
        ys = [float(_) for _ in ys]

    ax = plt.scatter(xs[-100:], ys[-100:])
    ax.axes.get_xaxis().set_visible(False)
    plt.savefig(output_folder / 'cpu.png')

import csv
import matplotlib.pyplot as plt
import psutil
from os.path import join
from time import time


def plot(input_folder, output_folder, log_folder, debug_folder):
    unix_time = time()
    cpu_percent = psutil.cpu_percent()

    with open(join(log_folder, 'cpu-usage.csv'), 'a+t') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([unix_time, cpu_percent])
        csv_file.seek(0)
        csv_reader = csv.reader(csv_file)
        xs, ys = zip(*csv_reader)
        xs = [float(_) for _ in xs]
        ys = [float(_) for _ in ys]

    ax = plt.scatter(xs, ys)
    ax.axes.get_xaxis().set_visible(False)
    plt.savefig(join(output_folder, 'cpu.png'))

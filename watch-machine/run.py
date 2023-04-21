import csv
from time import time

import matplotlib.pyplot as plt
import psutil


def plot_one(image_path, log_path, log_row):
    t = time() - TIME_IN_MINUTES * 60
    with open(log_path, 'a+t') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(log_row)
        csv_file.seek(0)
        xs = []
        ys = []
        for x, y in csv.reader(csv_file):
            x = float(x)
            y = float(y)
            if x < t:
                continue
            xs.append(x)
            ys.append(y)
    plt.figure()
    axes = plt.scatter(xs[-100:], ys[-100:]).axes
    axes.get_xaxis().set_visible(False)
    axes.set_ylabel('%')
    plt.savefig(image_path)


def plot_all(log_folder, output_folder):
    unix_time = time()
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    plot_one(output_folder / 'cpu.png', log_folder / 'cpu.csv', [
        unix_time, cpu_percent])
    plot_one(output_folder / 'ram.png', log_folder / 'ram.csv', [
        unix_time, ram_percent])


TIME_IN_MINUTES = 10

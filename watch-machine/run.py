import csv
from time import time

import matplotlib.pyplot as plt
import psutil


def plot_one(image_path, log_path, log_row):
    with open(log_path, 'a+t') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(log_row)
        csv_file.seek(0)
        csv_reader = csv.reader(csv_file)
        xs, ys = zip(*csv_reader)
        xs = [float(_) for _ in xs]
        ys = [float(_) for _ in ys]
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

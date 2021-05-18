import arrow
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from os.path import join


def load_table(path):
    t = pd.read_csv(
        path,
        parse_dates=['Date/Time'],
        date_parser=parse_timestamp)
    t.set_index('Date/Time', drop=True, inplace=True)
    # Update columns
    old_columns = t.columns
    new_columns = [_ for _ in old_columns if 'Monthly' not in _]
    t = t[new_columns].rename(columns={
        _: _.replace(' [kW](Hourly)', '') for _ in new_columns})
    return t


def split_table(table):
    column_names = table.columns

    def rename_electricity_column(column_name):
        column_name = column_name.replace(':Electricity', '')
        column_name = column_name.replace('Electricity:', '')
        column_name = column_name.replace('General:', '')
        column_name = column_name.replace(':InteriorEquipment', '')
        column_name = column_name.replace('Lights', ' Lights')
        column_name = column_name.replace(':WaterSystems', '')
        return column_name

    electricity_column_names = [_ for _ in column_names if 'Electricity' in _]
    electricity_table = table[electricity_column_names].rename(columns={
        _: rename_electricity_column(_) for _ in electricity_column_names
    })
    electricity_table.drop(columns=[
        'HVACFan:Fans',
        'Fans',
    ], inplace=True, errors='ignore')

    def rename_gas_column(column_name):
        column_name = column_name.replace(':Gas', '')
        column_name = column_name.replace('Gas:', '')
        return column_name

    gas_column_names = [_ for _ in column_names if 'Gas' in _]
    gas_table = table[gas_column_names].rename(columns={
        _: rename_gas_column(_) for _ in gas_column_names
    })
    return electricity_table, gas_table


def save_table_description(
        target_folder, table, customer_type, energy_type, category_name):
    target_path = join(
        target_folder,
        f'{customer_type}-{energy_type}-{category_name}-Description.csv')
    table.describe().round(2).to_csv(target_path)
    return target_path


def save_table_plot(
        target_folder, table, customer_type, energy_type, category_name,
        place_name):
    target_path = join(
        target_folder,
        f'{customer_type}-{energy_type}-{category_name}.png')
    datetime_series = pd.Series(table.index)
    x_values = datetime_series.quantile(np.linspace(0, 1, num=10))
    x_labels = [_.strftime('%m/%d %H:%M') for _ in x_values]
    ax = table.plot.area(figsize=(6, 4))
    ax.set_title(
        f'{place_name} {customer_type} {energy_type} {category_name}',
        loc='left')
    ax.legend(bbox_to_anchor=(1, 1))
    plt.xticks(x_values, x_labels, rotation=30)
    plt.xlabel('')
    plt.ylabel('kW')
    ax.plot()
    plt.savefig(target_path, bbox_inches='tight')
    plt.close()
    return target_path


def save_date_plot(
        target_folder, a_datestamp, b_datestamp, table, customer_type,
        energy_type, category_name, place_name):
    target_path = join(
        target_folder,
        f'{customer_type}-{energy_type}-{category_name}-' +
        f'{a_datestamp}-{b_datestamp}.png')
    t = table[
        (table.index > a_datestamp) &
        (table.index < b_datestamp)]
    ax = t.plot.area(figsize=(7, 3))
    ax.set_title(
        f'{place_name} {customer_type} {energy_type} {category_name} '
        f'{a_datestamp}',
        loc='left')
    ax.legend(bbox_to_anchor=(1, 1))
    plt.xlabel('Time')
    plt.ylabel('kW')
    ax.plot()
    plt.savefig(target_path, bbox_inches='tight')
    plt.close()
    return target_path


def parse_timestamp(timestamp):
    return arrow.get(
        '2000 ' + timestamp.strip(),
        'YYYY MM/DD  HH:mm:ss',
    ).datetime


def test_parse_timestamp():
    assert parse_timestamp(' 01/01  24:00:00').year == 2000

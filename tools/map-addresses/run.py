import geotable
from geopy.geocoders import GoogleV3
from os import environ
from os.path import join
from pandas import read_csv
from sys import argv


get_location = GoogleV3(environ['GOOGLE_KEY']).geocode


def get_longitude_latitude(address):
    location = get_location(address)
    return location.longitude, location.latitude


def augment_row(row):
    address = row['Address']
    longitude, latitude = get_longitude_latitude(address)
    row['Longitude'] = longitude
    row['Latitude'] = latitude
    return row


if __name__ == '__main__':
    input_folder, output_folder = argv[1:3]
    addresses_table = read_csv(join(input_folder, 'addresses.csv'))
    addresses_table = addresses_table.apply(augment_row, axis=1)
    addresses_table_path = join(output_folder, 'addresses.csv')
    addresses_table.to_csv(addresses_table_path, index=False)
    addresses_geotable = geotable.load(addresses_table_path)
    addresses_geotable.save_geojson(join(output_folder, 'addresses.geojson'))

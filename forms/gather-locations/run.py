import csv
import fcntl
import json
from geopy import Nominatim
from os.path import join
from sys import argv


# Get folder paths from command-line arguments
input_folder, output_folder = argv[1:]


# Load input variables from input folder
variables = json.load(open(join(input_folder, 'variables.json'), 'rt'))


# Perform calculation
geocode = Nominatim(user_agent='gather-locations').geocode
address = variables['address']
location = geocode(address)
longitude = location.longitude
latitude = location.latitude


# Save data
table_path = 'datasets/locations.csv'
with open(table_path, 'at') as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    csv_writer = csv.writer(f)
    csv_writer.writerow([address, longitude, latitude])


# Save output variables to output folder
json.dump({
    'longitude': longitude,
    'latitude': latitude,
}, open(join(output_folder, 'variables.json'), 'wt'))

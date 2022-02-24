import csv
import fcntl
import json
from geopy import Nominatim
from os.path import exists, join
from sys import argv


# Get folder paths from command-line arguments
input_folder, output_folder = argv[1:]


# Load input variables from input folder
variables = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))


# Perform calculation
geocode = Nominatim(user_agent='gather-locations').geocode
address = variables['address']
location = geocode(address)
longitude = location.longitude
latitude = location.latitude


# Save data
table_path = '../locations.csv'
is_new = not exists(table_path)
with open(table_path, 'at') as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    csv_writer = csv.writer(f)
    if is_new:
        csv_writer.writerow(['address', 'longitude', 'latitude'])
    csv_writer.writerow([address, longitude, latitude])


# Save output variables to output folder
json.dump({
    'longitude': longitude,
    'latitude': latitude,
}, open(join(output_folder, 'variables.dictionary'), 'wt'))

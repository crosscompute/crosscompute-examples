#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from invisibleroads_macros_disk import make_folder
from os import environ

input_folder = environ.get('CROSSCOMPUTE_INPUT_FOLDER', 'tests/standard/input')
output_folder = make_folder(environ.get('CROSSCOMPUTE_OUTPUT_FOLDER', 'tests/standard/output'))
debug_folder = make_folder(environ.get('CROSSCOMPUTE_DEBUG_FOLDER', 'tests/standard/debug'))


# In[ ]:


from os.path import join, exists

source_path = join(input_folder, 'variables.dictionary')
target_path = join(output_folder, 'configuration.json')
if 'JPY_PARENT_PID' not in environ and exists(target_path):
    exit()


# In[ ]:


import json
variables = json.load(open(source_path, 'rt'))
variables


# In[ ]:


from invisibleroads_macros_disk import unarchive_safely
from os.path import basename, exists, splitext
from urllib.request import urlretrieve as download

source_url = variables['url']
archive_name = basename(source_url)
archive_path = join(debug_folder, archive_name)
archive_folder = splitext(archive_path)[0]
if not exists(archive_folder):
    download(source_url, archive_path)
    unarchive_safely(archive_path, archive_folder)


# In[ ]:


from glob import glob
from pandas import read_excel

spreadsheet_paths = glob(join(archive_folder, '**/*.xlsx'), recursive=True)
if not spreadsheet_paths:
    raise Exception('could not find spreadsheet')
old_table = read_excel(spreadsheet_paths[0], engine='openpyxl')
new_table = old_table[['LON', 'LAT']]
new_table.to_json(join(output_folder, 'geometries.json'), orient='values')


# In[ ]:


import json

json.dump({
    'longitude': new_table.LON.mean(),
    'latitude': new_table.LAT.mean(),
    'zoom': 1,
}, open(join(output_folder, 'configuration.json'), 'wt'))


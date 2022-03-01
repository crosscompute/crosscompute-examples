#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import getenv

input_folder = getenv('CROSSCOMPUTE_INPUT_FOLDER', 'tests/base-10/input')
output_folder = getenv('CROSSCOMPUTE_OUTPUT_FOLDER', 'tests/base-10/output')


# In[ ]:


import json
from os.path import join

variables_dictionary = json.load(open(join(input_folder, 'variables.dictionary'), 'rt'))
variables_dictionary


# In[ ]:


base = variables_dictionary['base']
start = variables_dictionary['start']
stop = variables_dictionary['stop']
step = variables_dictionary['step']


# In[ ]:


import math

packs = []
if base == 'e':
    base = math.e
for x in range(start, stop + step, step):
    y = math.log(x, base)
    packs.append([x, y])
packs


# In[ ]:


json.dump({
    'columns': ['x', 'y'],
    'data': packs,
}, open(join(output_folder, 'values.json'), 'wt'))


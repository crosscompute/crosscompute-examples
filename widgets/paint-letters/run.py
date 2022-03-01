#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from os import getenv, makedirs
input_folder = getenv('CROSSCOMPUTE_INPUT_FOLDER', 'tests/standard/input')
output_folder = getenv('CROSSCOMPUTE_OUTPUT_FOLDER', 'tests/standard/output')
try:
    makedirs(output_folder)
except OSError:
    pass


# In[ ]:


from os.path import join
document_path = join(input_folder, 'document.txt')
document_text = open(document_path, 'rt').read().strip()
document_text


# In[ ]:


from collections import Counter
count_by_character = dict(Counter(document_text.lower()))
count_by_character


# In[ ]:


minimum_count = 0
maximum_count = max(count_by_character.values())
maximum_count


# In[ ]:


from matplotlib.colors import Normalize
normalize_count = Normalize(minimum_count, maximum_count)
normalize_count(3)


# In[ ]:


from matplotlib.pyplot import get_cmap
color_map = get_cmap('Reds')
color_map.N


# In[ ]:


color_map(color_map.N - 1)


# In[ ]:


from math import ceil
from matplotlib.colors import Normalize, to_hex

class ValueColor():
    
    def __init__(self, minimum_value, maximum_value, color_map):
        self.get_unit_value = Normalize(minimum_value, maximum_value)
        self.color_map = color_map
        self.color_map_maximum_value = color_map.N - 1
        
    def get_hex_color(self, value):
        unit_value = self.get_unit_value(value)
        color_map_value = ceil(unit_value * self.color_map_maximum_value)
        rgba = self.color_map(color_map_value)
        return to_hex(rgba)
    
value_color = ValueColor(minimum_count, maximum_count, color_map)
value_color.get_hex_color(1)


# In[ ]:


new_color_by_character = {k: value_color.get_hex_color(v) for k, v in count_by_character.items()}
new_color_by_character


# In[ ]:


image_template_path = 'datasets/letters.svg'
image_template_text = open(image_template_path, 'rt').read()


# In[ ]:


old_color_by_character = {
    'a': '#170b28',
    'b': '#3737c8',
    'c': '#212178',
    'd': '#442178',
    'e': '#800000',
    'f': '#5a2ca0',
    'g': '#7137c8',
    'h': '#8d5fd3',
    'i': '#ff8080',
    'j': '#aa87de',
    'k': '#c6afe9',
    'l': '#e3d7f4',
    'm': '#8787de',
    'n': '#5f5fd3',
    'o': '#ffaaaa',
    'p': '#ffd5d5',
    'q': '#2b0000',
    'r': '#aa0000',
    's': '#2d1650',
    't': '#d40000',
    'u': '#ff5555',
    'v': '#2c2ca0',
    'w': '#550000',
    'x': '#161650',
    'y': '#ff2a2a',
    'z': '#0b0b28',
}


# In[ ]:


character_by_old_color = {v: k for k, v in old_color_by_character.items()}


# In[ ]:


def get_new_color(match):
    old_color = match.group(0)
    character = character_by_old_color[old_color]
    if character in new_color_by_character:
        new_color = new_color_by_character[character]
    else:
        new_color = '#ffffff'
    return new_color


# In[ ]:


import re
HEX_COLOR_PATTERN = re.compile(r'#[0-9a-fA-F]{6}')
image_text = HEX_COLOR_PATTERN.sub(get_new_color, image_template_text)
open(join(output_folder, 'choropleth.svg'), 'wt').write(image_text)


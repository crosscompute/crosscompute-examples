import mimetypes
import json
from pathlib import Path
from sys import argv
from urllib.request import urlretrieve as download_uri

from PIL import Image
from reportlab.graphics import renderPM
from svglib.svglib import svg2rlg


input_folder, output_folder, debug_folder = [Path(
    _) for _ in argv[1:]]
with (input_folder / 'variables.dictionary').open('rt') as f:
    d = json.load(f)
image_uri = d['image_uri']
mime_type = mimetypes.guess_type(image_uri)[0]
file_extension = mimetypes.guess_extension(mime_type)
image_name = 'image' + file_extension
image_path = debug_folder / image_name
download_uri(image_uri, image_path)
converted_image_path = output_folder / 'image.png'
match file_extension:
    case '.svg':
        drawing = svg2rlg(image_path)
        renderPM.drawToFile(drawing, converted_image_path, fmt='png')
    case _:
        image = Image.open(image_path)
        image.save(converted_image_path)

import io
import json
import zipfile
from os import mkdir, walk
from os.path import join
from sys import argv

import fitz # PyMuPDF
import zipfile
from PIL import Image


def extract_pdf_images(input_path, output_path):
    with fitz.open(input_path) as pdf_reader:
        for page_index in range(len(pdf_reader)):
            page = pdf_reader[page_index]
            image_list = page.getImageList()
            if not image_list:
                continue
            for image_index, img in enumerate(page.getImageList(), start=1):
                xref = img[0]
                base_image = pdf_reader.extractImage(xref)
                image_bytes = base_image['image']
                image_ext = base_image['ext']
                image = Image.open(io.BytesIO(image_bytes))
                image_file_name = f'image{page_index+1}_{image_index}.{image_ext}'
                image_file_path = join(output_path, image_file_name)
                image.save(open(image_file_path, 'wb'))


def make_zip_file(zip_path, images_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_archive:
        for root, dirs, files in walk(images_path):
            for file_name in files:
                zip_archive.write(join(root, file_name), file_name)

def make_directory(directory_path):
    try:
        mkdir(directory_path)
    except OSError as error:
        pass
        # raise Exception('Error creating directory')


if __name__ == '__main__':
    input_folder = argv[1]
    output_folder = argv[2]
    input_path = join(input_folder, 'input.pdf')
    images_path = join(output_folder, 'images')
    zip_path = join(output_folder, 'images.zip')

    make_directory(images_path)
    extract_pdf_images(input_path, images_path)
    make_zip_file(zip_path, images_path)


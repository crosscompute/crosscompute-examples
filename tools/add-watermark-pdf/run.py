import json
from os.path import join
from sys import argv

from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PyPDF2 import PdfFileReader, PdfFileWriter


def make_watermark_pdf(watermark_path, watermark_pdf_path, w, h):
    image = Image.open(watermark_path)
    image_width, image_height = image.size
    image.putalpha(64)
    image.seek(0)
    transparent_image = ImageReader(image)
    pdf_width =  w/2 - (image_width/2)
    pdf_height = h/2 - (image_height/2)
    c = canvas.Canvas(watermark_pdf_path)
    c.setPageSize((w, h))
    c.drawImage(transparent_image, pdf_width, pdf_height, mask='auto')
    c.save()


def add_water_mark_to_pdf(input_path, output_path, watermark_path, watermark_pdf_path):
    pdf_reader = PdfFileReader(input_path)
    pdf_writer = PdfFileWriter()

    p = pdf_reader.getPage(0)
    w = float(p.mediaBox.getWidth())
    h = float(p.mediaBox.getHeight())
    make_watermark_pdf(watermark_path, watermark_pdf_path, w, h)

    watermark_obj = PdfFileReader(watermark_pdf_path)
    watermark_page = watermark_obj.getPage(0)

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output_path, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    input_folder = argv[1]
    output_folder = argv[2]
    input_path = join(input_folder, 'input.pdf')
    watermark_path = join(input_folder, 'watermark.png')
    watermark_pdf_path = join(input_folder, 'watermark.pdf')
    output_path = join(output_folder, 'output.pdf')

    add_water_mark_to_pdf(input_path, output_path, watermark_path, watermark_pdf_path)

import json
from os.path import join
from sys import argv
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.utils import PdfReadError


def remove_pdf_password(input_path, output_path, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_path)
    if pdf_reader.isEncrypted:
        pdf_reader.decrypt(password)

    try:
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))

        with open(output_path, 'wb') as fh:
            pdf_writer.write(fh)
    except:
        raise Exception('Check Password') 


if __name__ == '__main__':
    input_folder = argv[1]
    output_folder = argv[2]
    password_dictionary = json.load(open(join(input_folder, 'password.json')))
    password = password_dictionary['password']
    input_path = join(input_folder, 'input.pdf')
    output_path = join(output_folder, 'output.pdf')
    remove_pdf_password(input_path, output_path, password)

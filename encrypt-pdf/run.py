import json
from os.path import join
from sys import argv
from PyPDF2 import PdfFileReader, PdfFileWriter


def encrypt_pages_pdf(input_path, output_path, password):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_path)

    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))

    pdf_writer.encrypt(user_pwd=password, owner_pwd=None,
                       use_128bit=True)

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


if __name__ == '__main__':
    input_folder = argv[1]
    output_folder = argv[2]
    password_dictionary = json.load(open(join(input_folder, 'password.json')))
    password = password_dictionary['password']
    input_path = join(input_folder, 'input.pdf')
    output_path = join(output_folder, 'output.pdf')
    encrypt_pages_pdf(input_path, output_path, password)

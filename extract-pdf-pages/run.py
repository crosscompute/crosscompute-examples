import json
from os.path import join
from sys import argv
from PyPDF2 import PdfFileReader, PdfFileWriter


def extract_pdf_pages(input_path, output_path, pages):
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(input_path)
    pdf_last_page = pdf_reader.getNumPages()

    for page_number in pages:
        page_number_zero_indexed = page_number - 1
        if (page_number_zero_indexed > pdf_last_page):
            break
        print(page_number, pdf_last_page)
        pdf_writer.addPage(pdf_reader.getPage(page_number_zero_indexed))

    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)


def get_page_range_from_text(text):
    pageTextRange = text.split('-')
    if len(pageTextRange) == 2:
        try: 
            pageRangeLow = int(pageTextRange[0])
            pageRangeHigh = int(pageTextRange[1])
            if (pageRangeLow > pageRangeHigh):
                return 1, 0
            return pageRangeLow, pageRangeHigh
        except:
            pass
    return 1, 0 # not valid



def get_pages_from_text(pages_text):
    pagesArray = []
    for page_text in pages_text.split(','):
        try:
            pageNumber = int(page_text)
            pagesArray.append(pageNumber)
        except:
            pageRangeLow, pageRangeHigh = get_page_range_from_text(page_text)
            current = pageRangeLow
            while current <= pageRangeHigh:
                pagesArray.append(current)
                current += 1
    uniquePages = list(dict.fromkeys(pagesArray))
    uniquePages.sort()
    return uniquePages


if __name__ == '__main__':
    print(argv, len(argv))
    import pdb; pdb.set_trace()
    input_folder = argv[1]
    output_folder = argv[2]
    pages_dictionary = json.load(open(join(input_folder, 'pages.json')))
    pages_text = pages_dictionary['pages']
    input_path = join(input_folder, 'input.pdf')
    output_path = join(output_folder, 'output.pdf')
    extract_pdf_pages(input_path, output_path, get_pages_from_text(pages_text))

import PyPDF2
from PyPDF2 import PageObject

unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"

pdf = PyPDF2.PdfWriter()

page = pdf.add_blank_page(612, 800)


with open(changed_file, 'wb') as blank_file:
    pdf.write(blank_file)



with open(unchanged_file, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    pdf_writer = PyPDF2.PdfWriter()

    num_pages = len(pdf_reader.pages)

    output_page = blank_file

    for page_num in range(num_pages):
        source_page = pdf_reader.pages[page_num]

        output_page = PageObject.mergeTranslatedPage(source_page, 0, -page_num * 792,1)  

        pdf_writer.addPage(output_page)

    with open(r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\fg.pdf", 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

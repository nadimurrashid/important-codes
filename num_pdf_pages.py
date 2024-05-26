import PyPDF2

unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
pdf_file = open(unchanged_file, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

output_pdf = open(changed_file, 'wb')
pdf_writer = PyPDF2.PdfWriter()


page_width = 595  # A4 paper width in points
page_height = 842  # A4 paper height in points
left_margin = 0  # Left margin in points
top_margin = 0  # Top margin in points

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]

    new_page = PyPDF2.PageObject.create_blank_page(width=page_width, height=page_height)

    tx = -left_margin
    tyed = page_height - page.mergePage(page) - top_margin

    transformation = PyPDF2.Transformation().translate(tx, tyed)

    new_page.mergeTranslatedPage(page, transformation=transformation)

    pdf_writer.addPage(new_page)

pdf_writer.write(output_pdf)

pdf_file.close()
output_pdf.close()

print("Pages combined without borders successfully.")

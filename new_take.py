import PyPDF2
unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"

pdf_files = [
    unchanged_file,
    changed_file,
]

output_pdf = PyPDF2.PdfWriter()

width = 595  
height = 842  
new_page = PyPDF2.PageObject.create_blank_page(width, height)

for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_file, "rb"))
    page = pdf_reader.getPage(0)  
    new_page.mergePage(page)  
output_pdf.addPage(new_page)

with open(changed_file, "wb") as output_file:
    output_pdf.write(output_file)

print("PDFs combined without borders successfully.")

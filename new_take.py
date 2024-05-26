import PyPDF2
unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
# Open the PDF file you want to combine

# Open the PDF files you want to combine
pdf_files = [
    unchanged_file,
    changed_file,
    # Add more input PDFs here
]

# Create a PDF writer object for the output PDF
output_pdf = PyPDF2.PdfWriter()

# Create a blank page with custom dimensions (adjust width and height as needed)
width = 595  # Width in points (8.5 inches)
height = 842  # Height in points (11 inches)
new_page = PyPDF2.PageObject.create_blank_page(width, height)

# Iterate through the input PDFs and add their content to the new page
for pdf_file in pdf_files:
    pdf_reader = PyPDF2.PdfFileReader(open(pdf_file, "rb"))
    page = pdf_reader.getPage(0)  # Get the first page of each input PDF
    new_page.mergePage(page)  # Merge the page onto the new page

# Add the new page to the output PDF
output_pdf.addPage(new_page)

# Save the output PDF
with open(changed_file, "wb") as output_file:
    output_pdf.write(output_file)

print("PDFs combined without borders successfully.")

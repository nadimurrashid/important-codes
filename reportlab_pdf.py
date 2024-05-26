import PyPDF2
from PyPDF2 import PageObject

unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
# Open the PDF file you want to combine

# Open the source PDF file
# Create a new PDF file
pdf = PyPDF2.PdfWriter()

# Create a blank page (8.5 x 11 inches by default)
page = pdf.add_blank_page(612, 800)

# Specify the page dimensions (optional)

# Save the blank PDF to a file
with open(changed_file, 'wb') as blank_file:
    pdf.write(blank_file)



# Open the source PDF file
with open(unchanged_file, 'rb') as pdf_file:
    # Create a PdfFileReader object for the source PDF
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Create a PdfFileWriter object for the output PDF
    pdf_writer = PyPDF2.PdfWriter()

    # Calculate the total number of pages in the source PDF
    num_pages = len(pdf_reader.pages)

    # Create a new PDF page to combine all source pages
    output_page = blank_file

    # Loop through each page in the source PDF
    for page_num in range(num_pages):
        source_page = pdf_reader.pages[page_num]

        # Place the source page onto the output page, one below the other
        output_page = PageObject.mergeTranslatedPage(source_page, 0, -page_num * 792,1)  # Offset by page height

        # Add the combined page to the output PDF
        pdf_writer.addPage(output_page)

    # Save the output PDF with all pages stacked on top of each other
    with open(r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\fg.pdf", 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

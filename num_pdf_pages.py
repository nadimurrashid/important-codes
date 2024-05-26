import PyPDF2

unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
# Open the PDF file you want to combine
pdf_file = open(unchanged_file, 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Create a new PDF file to store the combined pages
output_pdf = open(changed_file, 'wb')
pdf_writer = PyPDF2.PdfWriter()


# Define page size and margins (adjust these values as needed)
page_width = 595  # A4 paper width in points
page_height = 842  # A4 paper height in points
left_margin = 0  # Left margin in points
top_margin = 0  # Top margin in points

# Iterate through each page of the input PDF and add it to the new PDF
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]

    # Create a new blank page with custom size and no margins
    new_page = PyPDF2.PageObject.create_blank_page(width=page_width, height=page_height)

    # Calculate the translation values
    tx = -left_margin
    tyed = page_height - page.mergePage(page) - top_margin

    # Use Transformation to translate the page
    transformation = PyPDF2.Transformation().translate(tx, tyed)

    # Apply the transformation and merge the page onto the new page
    new_page.mergeTranslatedPage(page, transformation=transformation)

    # Add the new page to the output PDF
    pdf_writer.addPage(new_page)

# Save the combined PDF to the output file
pdf_writer.write(output_pdf)

# Close the input and output PDF files
pdf_file.close()
output_pdf.close()

print("Pages combined without borders successfully.")

from aspose.pdf import Document

unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\random.pdf"
import aspose

# Input PDF files (list of file paths)
input_pdf_files = [unchanged_file]

# Output PDF file path
output_pdf_path = changed_file

# Create a new Document object
combined_document = Document()

# Iterate through the input PDF files and add their pages to the combined document
for pdf_file in input_pdf_files:
    pdf_document = Document(pdf_file)
    for page in pdf_document.pages:
        combined_document.pages.add(page)

# Save the combined PDF as a single borderless page
combined_document.save(output_pdf_path)

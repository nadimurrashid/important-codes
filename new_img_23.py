from aspose.pdf import Document

unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\random.pdf"
import aspose

input_pdf_files = [unchanged_file]

output_pdf_path = changed_file

combined_document = Document()

for pdf_file in input_pdf_files:
    pdf_document = Document(pdf_file)
    for page in pdf_document.pages:
        combined_document.pages.add(page)

combined_document.save(output_pdf_path)

import fitz
# Open the PDF file

unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax_Secondary\Secondary_CA076_CAPITALALLOWANCESEXAMPLE76LIMITED_File_2_0.pdf"
blank_file_1 = r"C:\Users\Sazid\Downloads\secondary\Tax_Secondary\test_changed\x.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax_Secondary\test_changed\Secondary_CA076_CAPITALALLOWANCESEXAMPLE76LIMITED_File_2_0.pdf"


pdf_file_path = 'input.pdf'
pdf_document = fitz.open(unchanged_file)

for page_number in range(len(pdf_document)):
    page = pdf_document[page_number]

    text_instances = page.search_for("IRMark")

    for inst in text_instances:
        page.delete_instance(inst)

output_pdf_path = changed_file
pdf_document.save(output_pdf_path)

pdf_document.close()

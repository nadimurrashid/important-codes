from PyPDF2 import PdfReader, PdfWriter




unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax_Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
blank_file_1 = r"C:\Users\Sazid\Downloads\secondary\Tax_Secondary\test_changed\x.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax_Secondary\test_changed\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
collected_sentence = []
replacements = [
    ("3CIYVBRHRQMMY66JT4F57DPEBBEYNQHL", "new string")
]

import os
import fitz

search_text = "3CIYVBRHRQMMY66JT4F57DPEBBEYNQHL"
replace_text = "Test"

pdf_file = fitz.open(unchanged_file)
found = False
for page in pdf_file:
    draft = page.search_for(search_text.strip())
    if draft:
        found = True
        for rect in draft:
            annot = page.add_redact_annot(rect,text=replace_text)
        page.apply_redactions()
        page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE)
    if found:
        output_file_name = changed_file
        pdf_file.save(output_file_name, garbage=4, deflate=True)
print(found)
pdf_file.close()
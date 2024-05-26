
import re
import fitz
import PyPDF2
import glob
path = sr.Get_Shared_Variables("base_pdf")
new_path = sr.Get_Shared_Variables("modified_base_pdf")
x = glob.glob(f"{path}\*.pdf")
t = []
for i in x:
    t.append(i.split('\\')[-1])


for pdfs in t:

    unchanged_file = f"{path}\\{pdfs}"
    blank_file_1 = f"{new_path}\\x.pdf"
    changed_file = f"{new_path}\\{pdfs}"

    collected_sentence = []

    with open(unchanged_file, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        pdf_writer = PyPDF2.PdfWriter()

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]

            page_text = page.extract_text()
            print(page_text)
            if "IRMark:" in page_text:
                target_text = "IRMArk"

                collected_text = re.findall(r'IRMark:(.*?[.!?])', page_text)

                new_text = ' '.join((collected_text))

                collected_sentence.append(new_text)

                pdf_writer.add_page(page)
    print(collected_sentence)

    list_with_only_IRMark = []

    for irmark in collected_sentence:
        list_with_only_IRMark.append(irmark)

    print(list_with_only_IRMark)

    pdf_file = fitz.open(unchanged_file)
    for new_retext in list_with_only_IRMark:
        pdf_file = fitz.open(unchanged_file)

        search_text = new_retext
        replace_text = " "

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

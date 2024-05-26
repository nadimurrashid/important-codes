import PyPDF2
import fitz  # PyMuPDF
from PyPDF2 import PageObject

unchanged_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"
changed_file = r"C:\Users\Sazid\Downloads\secondary\Tax Secondary\test_changed\Secondary_CA_TR001_CURRENT_FYACLAIM&GENERALPOOL_File_1_0.pdf"

reader = PyPDF2.PdfReader(unchanged_file)

print(len(reader.pages))

single_page = reader.pages[4]
print(single_page.cropbox.lower_left)
print(single_page.cropbox.upper_left)
print(single_page.cropbox.upper_right)
print(single_page.cropbox.lower_right)
print(841.91998/72)
print(594.95996/72)

writer = PyPDF2.PdfWriter()

for i in range(len(reader.pages)):
    page = reader.pages[i]
    page.cropbox.upper_left = 180
    writer.add_page(page)

outstream = open(changed_file,'wb')
writer.write(outstream)
outstream.close()




import sys
import difflib
from bs4 import BeautifulSoup
import html_diff
compared_list=["",""]
text = [[],[]]
files = []
soups = []
files_list=[r"A:\taxcalc_paths\xhtml_test\Base_FFS_GROUPFRS1021ATEST1_xbrli.xhtml",r"A:\taxcalc_paths\xhtml_test\Secondary_FFS_GROUPFRS1021ATEST1_xbrli.xhtml"]
path = r"A:\taxcalc_paths\xhtml_test\new_result.txt"
i=0
for file in files_list:
    files.append(open(file, "r").read())
    soups.append(BeautifulSoup(files[i], 'xml'))
    for tag_text in soups[i].find_all('xbrli:unit'):
        text[i].append(''.join(str(tag_text)))
        compared_list[i]+='\n'+str(tag_text)
    i+=1

result=""
for first_string, second_string in zip(text[0], text[1]):
    d = difflib.Differ()
    diff = d.compare(first_string.splitlines(), second_string.splitlines())
    result+='\n'.join(diff)

# f1 = open(files_list[0]).read()
# f2 = open(files_list[0]).read()
try:
    # diff_html = html_diff.diff('\n'.join(text[0]), '\n'.join(text[1]))
    with open(path, "w") as f:
        f.write(result)
except Exception as ex:
    print(ex)

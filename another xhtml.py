# from difflib import HtmlDiff
#
line1 = r"A:\taxcalc_paths\xhtml_test\Base_FFS_GROUPFRS1021ATEST1_xbrli.xhtml"
line2 = r"A:\taxcalc_paths\xhtml_test\Secondary_FFS_GROUPFRS1021ATEST1_xbrli.xhtml"
path = r"A:\taxcalc_paths\xhtml_test\new_result.html"
#
# d = HtmlDiff()
# difference = d.make_file(line1, line2)
# with open(path, "w") as f:
#     f.write()

# import difflib
#
# config1 = open(line1).readlines()
# config2 = open(line2).readlines()
#
# diff_html = difflib.HtmlDiff().make_file(config1, config2)
#
# with open(path, 'w') as opened_file:
#     opened_file.write(diff_html)


import difflib
from pathlib import Path

first_file_lines = Path(line1).read_text().splitlines()
second_file_lines = Path(line2).read_text().splitlines()

html_diff = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines)
Path(path).write_text(html_diff)

base_path= sr.Get_Shared_Variables("base_ixbrli_location")
secondary_path = sr.Get_Shared_Variables("secondary_ixbrli_location")
client_code = sr.Get_Shared_Variables("client_code[0]")
report_generation_path = sr.Get_Shared_Variables("xhtml_report")

FFSline1 = base_path + "\\" + "Base_FFS_" + client_code + "_xbrli.xhtml"

FFSline2 = secondary_path + "\\"  + "Secondary_FFS_"+ client_code +"_xbrli.xhtml"

report =  report_generation_path + "\\" + "FFS_REPORT_" + client_code + ".xhtml"

import difflib
from pathlib import Path



first_file_lines = Path(FFSline1).read_text().splitlines()

second_file_lines = Path(FFSline2).read_text().splitlines()

html_diff = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines)

Path(report).write_text(html_diff)
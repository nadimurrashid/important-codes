import re

text = """Capital Allowances Example 5 Limited UTR: 5896733794 IRMark: KIDFRW26OKYBC6GO2VRPZAM7PFLDXLDW. Page 2 of 7. This is the next sentence. Another sentence here!"""

# Define a regular expression pattern to find "IRMark" and capture text until the next full sentence
pattern = r'IRMark:(.*?[.!?])'

# Use re.search to find the first match
match = re.search(pattern, text, re.DOTALL)

if match:
    text_after_IRMark = match.group(1).strip()
    print(text_after_IRMark)
else:
    print("IRMark not found in the text.")

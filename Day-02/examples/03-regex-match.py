import re

text = "The quick brown fox"
pattern = r"quick" 

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

# match compares with the first object of string
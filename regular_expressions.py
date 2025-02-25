import re
pattern = r'\d+'
text = 'There are 3 apples'
match = re.search(pattern, text)
if match:
    print(match.group())
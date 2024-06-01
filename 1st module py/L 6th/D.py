import re
pattern = re.compile('https://')
print(re.fullmatch(pattern,'https://'))

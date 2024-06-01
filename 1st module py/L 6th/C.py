import re
import sys
def convert_date(date_string):
    pattern = re.compile(r'\d{2,}')
    match = re.findall(pattern, date_string)
    return match[2] + '-' + match[1] + '-' + match[0]
print(convert_date("2026-01-02"))

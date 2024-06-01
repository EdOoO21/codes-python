import re
def check_good_word(n):
    pattern = re.compile(r'[^a-zA-Z0-9 ]')
    match = re.findall(pattern, n)
    if len(match) != 0:
        return 'NO'
    else:
        return 'YES'



print(check_good_word("scgs gsihgswb gihSBG"))
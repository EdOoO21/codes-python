s = 'кант'
count = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        if word.count('к') == 2:
                            count+=1
                            print(word)
print(count)
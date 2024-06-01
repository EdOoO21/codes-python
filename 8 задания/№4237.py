s = 'ДЕЙКСТРА'
k = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = a + b + c + d + e + f
                        if (word.count('Й') == 1) and f != 'Й' and (word.count('ЙР') or word.count('ЙД') or word.count('ЙК') or word.count('ЙС') or word.count('ЙТ') == 1) and (a!=b and a!=c and a!=d and a!=e and a!=f and b!=c and b!=d and b!=e and b!=f and c!=d and c!=e and c!=f and d!=e and d!=f and e!=f):
                            k+=1
                            print(word)
print(k)
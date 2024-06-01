def f(s, marsh):
    global otvet
    global end
    if s == end and len(marsh) > 1:
        print(marsh)
        otvet += 1
    else:
        if marsh.count(s) > 1:
            return False
        for x in d[s]:
            print(s, x)
            f(x, marsh + x)


d = {'А': 'БГ',
     'Б': 'Д',
     'В': 'ГАД',
     'Г': 'ЖЕ',
     'Д': 'ИЛЕ',
     'Е': 'ЛВ',
     'Ж': 'Е',
     'И': 'Л',
     'Л': 'КЖ',
     'К': 'Ж',
     }

otvet = 0
start = 'Е'
end = 'Е'
f(start, start)
print(otvet)

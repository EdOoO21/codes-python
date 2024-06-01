def f(s, marsh):
    global otvet
    global end
    if s == end and len(marsh) > 1:
        print(marsh)
        otvet+=1
    else:
        if marsh.count(s) > 1:
            return False
        for x in d[s]:
            f(x, marsh + x)


d = {'А':'Б',
     'Б': 'ЕВ',
     'В': 'ГЗ',
     'Г': 'З',
     'Д': 'АБЕК',
     'Е': 'ЖВК',
    'Ж': 'ВК',
'З': 'МЛ',
'И': 'Д',
'Л': 'КЖ',
'К': 'И',
'М': 'Л',
     }
otvet=0
start='Ж'
end='Ж'
f(start,start)
print(otvet)


def f(s, marsh):
    global otvet

    if s == 'М' and len(marsh) > 1:
        if 'Е' not in marsh:
            otvet += 1
    else:
        if marsh.count(s) > 1:
            return 0
        for x in d[s]:
            f(x, marsh + x)


d = {
    'А': 'БГД',
    'Б': 'В',
    'В': 'И',
    'Г': 'БВЕ',
    'Д': 'ГЕЖЗ',
    'Е': 'ВИМЖ',
    'Ж': 'З',
    'З': 'МЛ',
    'К': 'М',
    'И': 'КМ',
    'Л': 'М',
    'М': ''
}

otvet = 0

f('А', 'А')

print(otvet)

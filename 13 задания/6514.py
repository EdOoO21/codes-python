def f(s, marsh):
    global otvet

    if s == 'Ж' and len(marsh) > 1:

        otvet += 1
    else:
        if marsh.count(s) > 1:
            return 0
        for x in d[s]:
            f(x, marsh + x)


d = {
    'А': 'Б',
    'Б': 'ВЕ',
    'В': 'ГЗЖ',
    'Г': 'З',
    'Д': 'АБ',
    'Е': 'ДКЖВ',
    'Ж': 'К',
    'З': 'МЖЛ',
    'К': 'ИД',
    'И': 'Д',
    'Л': 'ЖК',
    'М': 'Л'
}

otvet = 0

f('М', 'М')

print(otvet)

gl = 'АЕИ'


def f(s, marsh):
    global otvet

    if s == 'М' and len(marsh) > 1:
        fl = 0
        print(marsh)
        for i in range(len(marsh)):
            if marsh[i] in gl and marsh[i + 1] in gl:
                fl = 1
                break
        if fl == 0:
            otvet += 1
            print(marsh)
    else:
        if marsh.count(s) > 1 or s == 'М':
            return 0
        for x in d[s]:
            f(x, marsh + x)


d = {
    'А': 'БГЕДВ',
    'Б': 'Г',
    'В': 'Д',
    'Г': 'ЗЕ',
    'Д': 'ЖИ',
    'Е': 'ЛИ',
    'Ж': 'ЕИ',
    'З': 'КЛЕ',
    'К': 'ЛМ',
    'Л': 'ИМ',
    'И': 'М',
}

otvet = 0

f('А', 'А')

print(otvet)

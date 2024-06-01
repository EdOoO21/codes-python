def f(s,marsh):
    global otvet

    if s == 'Г' and len(marsh) > 1:
        if 'Б' not in marsh:
            otvet += 1
    else:
        if marsh.count(s) > 1:
            return 0
        for x in d[s]:
            f(x,marsh + x)


d = {
'А': 'В',
    'Б': 'АД',
    'В': 'Е',
    'Г': 'ВБД',
    'Д': 'З',
    'Е': 'Ж',
    'Ж': 'ГК',
    'З': 'Ж',
    'К': 'З',
}

otvet = 0

f('Г','Г')

print(otvet)
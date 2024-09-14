def f(s, marsh):
    global m
    if s == 'Ж' and len(marsh) > 1:
        m = max(m, len(marsh) - 1)
    else:
        if marsh.count(s) > 1:
            return 0
        for x in d[s]:
            f(x, marsh + x)


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

m = 0

f('Ж', 'Ж')
print(m)

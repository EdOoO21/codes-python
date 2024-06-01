def f(s,marsh):
    global otvet
    if s == 'Ж' and len(marsh) > 1:
        print(marsh)
        otvet += 1
    else:
        if marsh.count(s) > 1:
            return False
        for x in d[s]:
            f(x,marsh + x)

d = {
    'А':'БВ',
'Б':'Г',
'В':'Б',
'Г':'Ж',
'Д':'АВЗ',
'Е':'А',
'Ж':'ВДЗИ',
'З':'ЕИ',
'И':'К',
'К':'ЖГ',
}
otvet = 0
f('Ж','Ж')
print(otvet)
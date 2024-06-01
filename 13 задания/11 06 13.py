def f(s,marsh):
    global otvet

    if s == 'М' and 'З' in marsh and 'Л' in marsh:
        otvet += 1
        print(marsh)
    else:
        if s == 'М' or s == 'Н':
            return 0
        else:
            for x in d[s]:
                f(x,marsh + x)

d = {
    'А':'Е',
'Б':'АЕВЗД',
'В':'ЗГ',
'Г':'И',
'Д':'ЕЖЗ',
'Е':'Ж',
'Ж':'ЗКЛ',
'З':'ГИК',
'И':'КМ',
'К':'ЛМ',
'М':'Н',
'Н':'',
'Л':'МН',


}

otvet = 0

f('Б','Б')

print(otvet)

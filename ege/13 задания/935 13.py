def f(s,marsh):
    global otvet

    if s == 'М' and len(marsh) > 1 and 'Е' in marsh:
        otvet += 1
        print(marsh)

    else:
        if marsh.count(s) > 1:
            return 0
        else:
            for x in d[s]:
                f(x,marsh + x)

d = {
    'А':'БГД',
'Б':'В',
'В':'И',
'Г':'БВЕ',
'Д':'ГЕЖЗ',
'Е':'ВИМЖ',
'Ж':'З',
'З':'МЛ',
'И':'КМ',
'К':'М',
'Л':'М',
'М':'',
}

otvet = 0
f('А','А')
print(otvet)
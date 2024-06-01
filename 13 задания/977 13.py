def f(s, marsh):
    global otvet

    if s == 'Е' and len(marsh) > 1:
        otvet += 1
        print(marsh)

    else:
        if marsh.count(s) > 1:
            return 0
        else:
            for x in d[s]:
                f(x, marsh + x)


d = {
    "А": "ГБ",
    "Б": "Д",
    "В": "ГБДА",
    "Г": "ЖЕ",
    "Д": "ЕЛИ",
    "Е": "ВЛ",
    "Ж": "Е",
    "И": "Л",
    "К": "Ж",
    "Л": "КЖ",

}

otvet = 0

f('Е', 'Е')

print(otvet)

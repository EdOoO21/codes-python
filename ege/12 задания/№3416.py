l = '3' + 57*'5'
while '25' in l or '355' in l or '4555' in l:
    l = l.replace('25','3',1)
    l = l.replace('355','4',1)
    l = l.replace('4555','2',1)
print(l)
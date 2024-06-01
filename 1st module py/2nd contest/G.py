s = ' ' + str(input()) + ' '
s = s.replace(' ', '  ')
print(s.count('  ') - (s.count('-') + s.count(' 0 ')) - 1)

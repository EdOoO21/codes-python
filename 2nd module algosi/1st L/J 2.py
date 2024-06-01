a = (str(input()) + ' ' + str(input()) + ' ' + str(input())).split()


def line_check(k, a):
    if len({a[k], a[k + 1], a[k + 2]}) == 1:
        return a[k]
    return '0'


def col_check(k, a):
    if len({a[k], a[k + 3], a[k + 6]}) == 1:
        return a[k]
    return '0'


def crossdown_check(a):
    if len({a[0], a[4], a[8]}) == 1:
        return a[0]
    return '0'


def crossup_check(a):
    if len({a[2], a[4], a[6]}) == 1:
        return a[2]
    return '0'


if not (1 >= (a.count('1') - a.count('2')) >= 0):
    print('NO')

elif ((line_check(0, a) + line_check(3, a) + line_check(6, a)).count('1') != 0) \
        and ((line_check(0, a) + line_check(3, a) + line_check(6, a)).count('2') != 0):
    print('NO')

elif ((col_check(0, a) + col_check(1, a) + col_check(2, a)).count('1') != 0) \
        and ((col_check(0, a) + col_check(1, a) + col_check(2, a)).count('2') != 0):
    print('NO')

elif ((line_check(0, a) + line_check(3, a) + line_check(6, a)).count('2') != 0) and (a.count('2') != a.count('1')):
    print('NO')

elif ((col_check(0, a) + col_check(1, a) + col_check(2, a)).count('2') != 0) and (a.count('2') != a.count('1')):
    print('NO')

elif ((line_check(0, a) + line_check(3, a) + line_check(6, a)).count('1') != 0) and (a.count('2') + 1 != a.count('1')):
    print('NO')

elif ((col_check(0, a) + col_check(1, a) + col_check(2, a)).count('1') != 0) and (a.count('2') + 1 != a.count('1')):
    print('NO')

elif ((crossdown_check(a)).count('1') != 0) and (a.count('2') + 1 != a.count('1')):
    print('NO')
elif ((crossup_check(a)).count('1') != 0) and (a.count('2') + 1 != a.count('1')):
    print('NO')
elif ((crossdown_check(a)).count('2') != 0) and (a.count('2') != a.count('1')):
    print('NO')
elif ((crossup_check(a)).count('2') != 0) and (a.count('2') != a.count('1')):
    print('NO')

else:
    print('YES')

a = (str(input()) + ' ' + str(input()) + ' ' + str(input())).split()
print(a)
p = (((len({a[0], a[1], a[2]}) == 1) and (a[0] != '0')) + ((len({a[3], a[4], a[5]}) == 1) and (a[4] != '0')) + (
            (len({a[6], a[7], a[8]}) == 1) and (a[6] != '0')) + ((len({a[0], a[3], a[6]}) == 1) and (a[6] != '0')) + (
                (len({a[1], a[4], a[7]}) == 1) and (a[1] != '0')) + (
                (len({a[2], a[5], a[8]}) == 1) and (a[2] != '0')) + (
                (len({a[0], a[4], a[8]}) == 1) and (a[0] != '0')) + (
                (len({a[2], a[4], a[6]}) == 1) and (a[6] != '0')))
if (0 <= (a.count('1') - a.count('2'))) and ((a.count('1') - a.count('2')) <= 1):
    if p == 1:
        ans = [p]
        ans1 = [{a[0], a[1], a[2]}, {a[3], a[4], a[5]}, {a[6], a[7], a[8]}, {a[0], a[3], a[6]}, {a[1], a[4], a[7]},
                {a[2], a[5], a[8]}, {a[2], a[4], a[6]}]
        ans1 = ans1[ans.index(True)]
        if ans1 == {'1'}:
            if (a.count('1') - a.count('2')) == 1:
                print('YES')
            else:
                print('NO')
        else:
            if (a.count('1') - a.count('2')) == 0:
                print('YES')
            else:
                print('NO')
    elif p == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')

# elif ((a[0] == a[4]) and (a[4]== a[7]) and (a[7] == a[0])) and a[0] != 0:
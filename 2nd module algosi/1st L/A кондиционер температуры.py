troom, tcond = map(int, str(input()).split())
work_type = str(input())
if work_type == 'freeze':
    if troom > tcond:
        print(tcond)
    else:
        print(troom)

if work_type == 'heat':
    if troom < tcond:
        print(tcond)
    else:
        print(troom)

if work_type == 'auto':
    print(tcond)

if work_type == 'fan':
    print(troom)

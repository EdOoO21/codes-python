from fnmatch import fnmatch

string = str(input())
if (set(string) == {' '}) or (not string):  # пустая
    print(string)

elif string[0] != '<':  # первая не <
    print('<' + string[1:])

elif string[-1] != '>':  # последняя не >
    print(string[:-1] + '>')
####################################################################################################################################################################################################################
####################################################################################################################################################################################################################
####################################################################################################################################################################################################################
####################################################################################################################################################################################################################
else:
    st = string.split('<')
    st.pop(0)
    if string.count('<') > string.count('>'):

        if string.count('<') % 2 == 1:  # добавили <

            if '<>' in string:
                test_string = st[(st.index('>')) - 1]
                if test_string[0] == '/':
                    test_string = test_string[1:]
                    for i in st:
                        if fnmatch(i, test_string + '?>') and (('/' + i) not in st):  # поиск нужных букв
                            st[(st.index('>')) - 1] = '/' + i
                            break
                else:
                    for i in st:
                        if fnmatch(i[1:], test_string + '?>') and (i[1:] not in st):  # поиск нужных букв
                            st[(st.index('>')) - 1] = i[1:]
                            break

                st.remove('>')
                st[0] = '<' + st[0]
                print(*st, sep='<')
            elif '<<' in string:
                test_string = st[(st.index('')) + 1]
                ans = ''
                for i1 in st:
                    if fnmatch(i1, test_string) and (('/' + test_string) not in st) and (
                            i1 is not test_string):  # для <dbc><<dbc>
                        st[(st.index('')) + 1] = '/' + i1
                        break
                    elif fnmatch(i1[2:], test_string) and (i1[0] == '/') and (i1[1:] not in st):  # для <<bc></dbc>
                        st[(st.index('')) + 1] = i1[1:]
                        break
                if string.count('<') != string.count('>'):
                    for i in range(len(st)):
                        if st[i][-1] != '>':
                            st[i] = st[i] + '>'
                            break
                st.remove('')
                st[0] = '<' + st[0]
                print(*st, sep='<')

            else:  # добавили в рандом место < но не рядом со скобкой
                test_string = [x for x in st if x[-1] != '>']
                test_string.append(st[st.index(test_string[0]) + 1])
                st.pop(st.index(test_string[0]) + 1)
                if test_string[0][0] != '/':
                    for i in st:
                        if fnmatch(i, '/' + test_string[0] + '?' + test_string[1]) and (i[1:] not in st):
                            st[st.index(test_string[0])] = i[1:]
                            break
                else:
                    for i in st:
                        if fnmatch(i, test_string[0][1:] + '?' + test_string[1]) and ('/' + i not in st):
                            st[st.index(test_string[0])] = '/' + i
                            break

                st[0] = '<' + st[0]
                print(*st, sep='<')

        else:  # убрали >
            for i in range(len(st)):
                if st[i][-1] != '>':
                    st[i] = st[i][:-1] + '>'
                    break
            st[0] = '<' + st[0]
            print(*st, sep='<')
    elif string.count('<') < string.count('>'):

        if string.count('>') % 2 == 1:  # добавили >
            if '<>' in string:
                test_string = [x[1:] for x in st if x[0] == '>']
                if test_string[0] in st:
                    st[st.index('>' + test_string[0])] = '/' + test_string[0]

                else:
                    for i in st:
                        if fnmatch(i[2:], test_string[0]) and (i[1:] not in st):
                            st[st.index('>' + test_string[0])] = i[1:]
                            break
                st[0] = '<' + st[0]
                print(*st, sep='<')

            elif '>>' in string:
                if (string.count('>') - string.count('<')) != 2:
                    test_string = [x[:-2] for x in st if (x[-2] == '>') and (x[-1] == '>')]

                    if test_string[0][0] != '/':
                        for i in st:
                            if fnmatch(i[1:], test_string[0] + '?' + '>') and (i[1:] not in st):
                                st[st.index(test_string[0] + '>>')] = i[1:]
                                break
                    else:
                        for i in st:
                            if fnmatch(i, test_string[0][1:] + '?' + '>') and (('/' + i) not in st):
                                st[st.index(test_string[0] + '>>')] = '/' + i
                                break
                    st[0] = '<' + st[0]
                    print(*st, sep='<')
                else:
                    for i in range(len(st)):
                        if st[i].count('>') == 3:
                            st[i] = st[i].replace('>>', '><', 1)
                            break
                    st[0] = '<' + st[0]
                    print(*st, sep='<')

            else:
                test_string = [x for x in st if x.count('>') > 1]
                index = st.index(test_string[0])
                test_string = test_string[0].split('>')
                test_string.pop(-1)
                test_string[-1] += '>'
                if test_string[0][0] == '/':
                    for i in st:
                        if fnmatch(i, test_string[0][1:] + '?' + test_string[1]) and (('/' + i) not in st):
                            st[index] = '/' + i
                            break
                else:
                    for i in st:
                        if fnmatch(i[1:], test_string[0] + '?' + test_string[1]) and (i[1:] not in st):
                            st[index] = i[1:]
                            break
                st[0] = '<' + st[0]
                print(*st, sep='<')

        else:  # если убрали <
            st = string.split('>')
            st.pop(-1)

            for i in range(len(st)):
                if st[i][0] != '<':
                    st[i] = '<' + st[i][1:]
                    break
            st[-1] = st[-1] + '>'
            print(*st, sep='>')

    else:
        st = [x[:-1] for x in st]
        with_slash = [x for x in st if x[0] == '/']
        test_string = [x for x in st if x[0] != '/']

        if len(test_string) == len(with_slash):
            ans = ''
            for i in test_string:
                if ('/' + i) not in st:
                    ans = i
                    break
            if ans == '':
                for i in range(len(with_slash)):
                    if with_slash[i][1:] not in st:
                        ans = with_slash[i]
                        sup_index = i
                        break
                
        #
        # elif len(test_string) > len(with_slash):





        # else:


    # <abcde></abcde><fabcde></fabcde><abcde><fabcde>


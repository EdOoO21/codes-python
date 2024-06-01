n = int(input())
st = str(input())
st = st[::-1]
while st != '':
    try:
        l = st[:st.index(' ')]
    except ValueError:
        print(st[::-1],end='')
        st = ''
    else:
        print(l[::-1],end=' ')
        st = st[st.index(' ') + 1:]



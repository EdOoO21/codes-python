a = str(input())
stack = []
for i in a:
    if i in '[{(':
        stack.append(i)
    elif i in ']})':
        if len(stack) == 0:
            print('no')
            break
        if i == ')':
            if stack[-1] != '(':
                print('no')
                break
            else:
                stack.pop(-1)
        if i == ']':
            if stack[-1] != '[':
                print('no')
                break
            else:
                stack.pop(-1)
        if i == '}':
            if stack[-1] != '{':
                print('no')
                break
            else:
                stack.pop(-1)
else:
    if not stack:
        print('yes')
    else:
        print('no')




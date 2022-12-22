while True:
    S = input()
    if S == '.':
        break
    d = []
    flag = 0
    for s in list(S):
        if s in ['[', '(']:
            d.append(s)
        if s == ']':
            if '[' not in d:
                flag = -1
            elif d[-1] == '[':
                d.pop()
            else:
                flag = -1
        if s == ')':
            if '(' not in d:
                flag = -1
            elif d[-1] == '(':
                d.pop()
            else:
                flag = -1
    if d:
        flag = -1
    if flag == 0:
        print('yes')
    else:
        print('no')

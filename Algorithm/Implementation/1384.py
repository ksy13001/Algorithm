t = 0
while True:
    t += 1
    n = int(input())
    good = True
    if n == 0: break
    else: print('Group', t)
    name = []
    note = []
    for _ in range(n):
        arr = list(map(str, input().split()))
        name.append(arr[0])
        note.append(arr[1:])
    for i in range(n):
        for j in range(1,n):
            if note[i][j-1] == 'N':
                good = False
                print(f'{name[name.index(name[i])-j]} was nasty about {name[i]}')
    if good:
        print('Nobody was nasty')
    print()

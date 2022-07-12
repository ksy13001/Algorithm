n = int(input())
mo = sorted(list(map(int, input().split())))
group = 0
while mo:
    m = mo.pop()
    if len(set(mo)) == 1:
        group += 1
        break
    for i in range(1, m):
        if i in mo:
            mo.remove(i)
    group += 1
print(group)

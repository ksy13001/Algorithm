n, m = map(int, input().split())

target = set(map(int, input().split()[1:]))
ans = 0
arr = []
if 0 in target:
    ans = m
else:
    for _ in range(m):
        k = set(map(int, input().split()[1:]))
        arr.append(k)
    for _ in range(m):
        for i in arr:
            if i & target:
                target = target.union(i)
    for i in arr:
        if i & target:
            continue
        else:
            ans += 1
print(ans)



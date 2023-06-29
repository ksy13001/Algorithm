n, m = map(int, input().split())
if n == 0:
    print(0)
else:
    book = list(map(int, input().split()))
    box = 1
    now = 0
    for i in range(n):
        if book[i] + now <= m:
            now += book[i]
        else:
            box += 1
            now = book[i]
    print(box)

def sol():
    n, m = map(int, input().split())

    for k in range(m, 101):
        ans = []
        if k % 2 == 1:
            if n % k == 0 and k <= n//k * 2 + 1:
                ans = list(range(n//k-(k//2), n//k+(k//2)+1))
                print(*ans)
                return
        else:
            if n % (k//2) == 0:
                now = n//(k//2)
                if now % 2 == 1:
                    if now//2 - (k//2)+1 <0:
                        continue
                    ans = list(range(now//2-(k//2)+1, now//2+(k//2)+1))
                    print(*ans)
                    return

    return print(-1)
while True:
    sol()


n, q = map(int, input().split())

arr = list(map(int, input().split()))
black = [False] * n
ans = 0
for i in range(q):
    now = arr[i] - 1
    if black[now]:
        black[now] = False
        if now - 1 >= 0 and black[now - 1] and now + 1 < n and black[now + 1]:
            ans += 1
        elif (now-1 < 0 or now - 1 >= 0 and not black[now - 1]) and (now + 1 >=n or now + 1 < n and not black[now + 1]):
            ans -= 1
    else:
        black[now] = True
        if (now-1 < 0 or now - 1 >= 0 and not black[now - 1]) and (now + 1 >=n or now + 1 < n and not black[now + 1]):
            ans += 1
        elif (now - 1 >= 0 and black[now - 1]) and (now + 1 < n and black[now + 1]):
            ans -=1

    print(ans)

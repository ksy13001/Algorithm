for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for _ in range(n):
        a, b, r = map(int,input().split())
        if ((x1 - a)**2 + (y1 - b)**2)**0.5 < r and ((x2 - a)**2 + (y2 - b)**2)**0.5 < r:
            continue
        elif ((x1 - a)**2 + (y1 - b)**2)**0.5 < r:
            cnt += 1
        elif ((x2 - a)**2 + (y2 - b)**2)**0.5 < r:
            cnt += 1
    print(cnt)

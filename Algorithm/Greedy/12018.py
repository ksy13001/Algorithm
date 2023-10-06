import sys
input = sys.stdin.readline


def sol():
    n, m = map(int, input().split())
    arr = []
    cnt = 0
    now = 0
    for _ in range(n):
        p, l = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort(reverse=True)
        if l-1 >= p:
            if m > 0:
                cnt += 1
                m -= 1
        else:
            if 1 <= a[l-1] <= 36:
                arr.append(a[l-1])
    arr.sort()
    for i in arr:
        m -= i
        if m < 0:
            break
        else:
            cnt += 1
    print(cnt)
    return

sol()

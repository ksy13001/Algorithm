import sys
input = sys.stdin.readline


def sol():
    n, m = map(int, input().split())
    if n > m:
        n = m
    arr = [int(input()) for _ in range(m)]
    arr.sort()
    ans = 0
    price = 0
    for i in range(m):
        k = arr[i] * min((m-i), n)
        if ans < k:
            ans = k
            price = arr[i]
    print(price, ans)


sol()

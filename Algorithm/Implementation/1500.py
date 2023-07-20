from math import prod


def sol():
    n, k = map(int, input().split())
    if n == k:
        return print(1)
    arr = [1] * k
    cnt = k
    while True:
        for i in range(k):
            arr[i] += 1
            cnt += 1
            if cnt == n:
                return print(prod(arr))


sol()

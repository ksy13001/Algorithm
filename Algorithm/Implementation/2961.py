from itertools import combinations


def cal(arr):
    k = int(1e9)
    for i in arr:
        x, y = 1, 0
        for s, b in i:
            x *= s
            y += b
        k = min(k, abs(x-y))
    return k


def sol():
    n = int(input())
    arr = []
    for _ in range(n):
        s, b = map(int, input().split())
        arr.append((s, b))
    ans = int(1e9)
    for i in range(1, n+1):
        com = list(combinations(arr, i))
        ans = min(ans, cal(com))
        if ans == 0:
            return 0
    return ans



print(sol())

import sys
INF = sys.maxsize
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = 0
    if n % 2 == 1:
        center = arr.pop()
        left = arr.pop()
        right = arr.pop()
        ans = max(ans, center - left, center - right)
    else:
        left = arr.pop()
        right = arr.pop()
    while arr:
        ln = arr.pop()
        rn = arr.pop()
        ans = max(ans, left - ln, right - rn)
        left = ln
        right = rn
    print(ans)
    return


for _ in range(int(input())):
    sol()

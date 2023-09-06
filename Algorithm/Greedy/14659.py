import sys, heapq
INF = sys.maxsize
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    now = arr[0]
    cnt = 0
    for i in range(1, n):
        if arr[i] < now:
            cnt += 1
        else:
            ans = max(ans, cnt)
            now = arr[i]
            cnt = 0
    ans = max(ans, cnt)
    print(ans)


sol()

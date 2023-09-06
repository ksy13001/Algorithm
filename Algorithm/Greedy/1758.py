import sys
INF = sys.maxsize
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort(reverse=True)
    ans = 0
    for i in range(n):
        if arr[i] - i <= 0:
            break
        else:
            ans += arr[i]-i
    print(ans)


sol()

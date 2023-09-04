import sys
INF = sys.maxsize
input = sys.stdin.readline


def sol():
    n = int(input().rstrip())
    arr = list(map(int, input().split()))
    cnt = 0
    loss = 0
    ans = 0
    max_num = max(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1] and arr[i] == max_num:
            ans += cnt * arr[i] - loss
            cnt = 0
            loss = 0
            max_num = max(arr[i+1:])
        else:
            loss += arr[i]
            cnt += 1
    if cnt > 0:
        ans += cnt * arr[-1] - loss
    print(ans)


for _ in range(int(input())):
    sol()

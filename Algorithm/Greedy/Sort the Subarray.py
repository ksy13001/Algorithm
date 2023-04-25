import sys
input = sys.stdin.readline

for _ in range(int(input())):
    up, down, now = -1, -1, -1
    cnt = 1
    n = int(input())
    arr = list(map(int, input().split()))
    sub = list(map(int, input().split()))
    for i in range(n):
        if arr[i] != sub[i]:
            up = i
            down = i
            break
    while down > 0:
        if sub[down] >= sub[down-1]:
            down -=1
        else:
            break
    while up < n-1:
        if sub[up] <= sub[up+1]:
            up += 1
        else:
            break
    print(down + 1, up + 1)

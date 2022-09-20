import sys
input = sys.stdin.readline
n = int(input())
arr = []
cnt = 1
for _ in range(n):
    x, y = map(int, input().split())
    arr.append((x, y))
arr.sort(key=lambda x: (x[1],x[0]))

now_end = arr[0][1]
for i in range(1, n):
    if now_end <= arr[i][0]:
        cnt += 1
        now_end = arr[i][1]

print(cnt)

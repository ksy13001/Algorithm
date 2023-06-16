import sys

input = sys.stdin.readline
H, W = map(int, input().split())
n = int(input())
arr = []
for _ in range(n):
    r, c = map(int, input().split())
    arr.append((r, c))
arr = sorted(arr, key=lambda x: x[0] * x[1], reverse=True)
ans = 0

for i in range(n - 1):
    tmp = 0
    for j in range(i + 1, n):
        if (max(arr[i][0], arr[j][0]) <= H and arr[i][1] + arr[j][1] <= W) or (
                max(arr[i][0], arr[j][0]) <= W and arr[i][1] + arr[j][1] <= H) or \
                (arr[i][0] + arr[j][0] <= H and max(arr[i][1], arr[j][1]) <= W) or (
                arr[i][0] + arr[j][0] <= W and max(arr[i][1], arr[j][1]) <= H) \
                or (max(arr[i][0], arr[j][1]) <= H and arr[i][1] + arr[j][0] <= W) or max(arr[i][0], arr[j][1]) <= W and \
                arr[i][1] + arr[j][0] <= H \
                or (arr[i][0] + arr[j][1] <= H and max(arr[i][1], arr[j][0]) <= W) or (
                arr[i][0] + arr[j][1] <= W and max(arr[i][1], arr[j][0]) <= H):
            tmp = arr[i][0] * arr[i][1] + arr[j][0] * arr[j][1]
            break
    ans = max(ans, tmp)
print(ans)

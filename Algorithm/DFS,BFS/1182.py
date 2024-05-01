n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ans = 0


def dfs(now, i):
    global ans
    if now == s:
        ans += 1
    if i == n:
        return
    for j in range(i+1, n):
        dfs(now+arr[j], j)


for i in range(n):
    dfs(arr[i], i)


print(ans)

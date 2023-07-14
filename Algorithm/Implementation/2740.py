n, m = map(int, input().split())
a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))
m, k = map(int, input().split())
for _ in range(m):
    b.append(list(map(int, input().split())))
ans = [[0 for _ in range(k)]for _ in range(n)]
# n = 3, m = 2, k = 3
for i in range(n):
    for j in range(m):
        for p in range(k):
            ans[i][p] += a[i][j] * b[j][p]
for i in range(n):
    print(*ans[i])

visited = [[False for _ in range(100)] for _ in range(100)]
ans = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if not visited[i][j]:
                ans += 1
                visited[i][j] = True
print(ans)

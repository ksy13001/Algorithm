import sys
input = sys.stdin.readline
n, m = map(int, input().split())
visited = [[0 for _ in range(100)]for _ in range(100)]
ans = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(100):
        for j in range(100):
            if x1-1 <= i <= x2-1 and y1-1 <= j <= y2-1 and visited[i][j] <= m:
                visited[i][j] += 1
                if visited[i][j] > m:
                    ans += 1
print(ans)

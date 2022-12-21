import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
road = [[] for _ in range(n+1)]
start = INF
end = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    road[a].append((b, c))
    road[b].append((a, c))
    start = min(c, start)
    end = max(c, end)
t1, t2 = map(int, input().split())


def bfs(visited, weight):
    q = deque()
    q.append(t1)
    while q:
        now = q.popleft()
        if now == t2:
            return True
        for node, value in road[now]:
            if not visited[node]:
                if value >= weight:
                    q.append(node)
                    visited[node] = True
    return False


ans = 0
while start <= end:
    visited = [False for _ in range(n+1)]
    mid = (start + end) // 2
    if bfs(visited, mid):
        start = mid + 1
        ans = mid
    else:
        end = mid - 1

print(ans) 

import sys
from collections import deque
input = sys.stdin.readline
v = int(input())
graph = [[]for _ in range(v+1)]
for _ in range(v):
    a = list(map(int, input().split()))
    for i in range(1, len(a)-2, 2):
        graph[a[0]].append((a[i], a[i+1]))


def bfs(start):
    visited = [0 for _ in range(v+1)]
    visited[start] = 0
    q = deque([start])
    while q:
        now = q.popleft()
        for node, dist in graph[now]:
            if visited[node] == 0 and node != start:
                visited[node] += dist + visited[now]
                q.append(node)
    return (max(visited), visited.index(max(visited)))


value, node = bfs(1)
v2, n2 = bfs(node)
print(v2)

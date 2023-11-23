import sys
from collections import deque
INF = sys.maxsize
input = sys.stdin.readline
n, s, e, m = map(int, input().split())
graph = []
node = [[] for _ in range(n)]


def bfs(start, end):
    q = deque([start])
    visited = [False for _ in range(n)]
    while q:
        now = q.popleft()
        if now == end:
            return True
        for i in node[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    return False


def bf(start):
    # 시작 부터 돈 벌기
    distance[start] = pay[start]
    for i in range(n):
        for j in range(m):
            now, next_node, cost = graph[j]
            if distance[now] != -INF and distance[next_node] < distance[now] + pay[next_node] - cost:
                distance[next_node] = distance[now] + pay[next_node] - cost
                if i == n-1:
                    if bfs(now, e):
                        return 'Gee'
    return distance[e]


for _ in range(m):
    a, b, c = map(int, input().split())
    node[a].append(b)
    graph.append((a, b, c))


pay = list(map(int, input().split()))
distance = [-INF] * n
ans = bf(s)

if distance[e] == -INF:
    print('gg')
else:
    print(ans)

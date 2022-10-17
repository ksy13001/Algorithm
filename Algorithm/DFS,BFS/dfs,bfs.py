from collections import deque
n, m, v = map(int, input().split())
graph = [[]for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()
visited = [False]*(n+1)
visited1 = [False]*(n+1)


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

#모든 간선값이 같을때 or 최단거리, 최소
#큐를 미리 채워도 됨, 큐에 좌표가아닌 다른 조건이 들어갈수도 있음
def bfs(graph, v, visited):
    que = deque([v])
    visited[v] = True
    while que:
        v = que.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


dfs(graph, v, visited)
print('')
bfs(graph, v, visited1)

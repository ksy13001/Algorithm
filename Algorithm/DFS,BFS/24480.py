import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0 for _ in range(n+1)]
cnt = 1


def dfs(visited, now):
    global cnt
    visited[now] = cnt
    cnt += 1
    for i in sorted(graph[now], reverse=True):
        if visited[i] == 0:
            dfs(visited, i)


dfs(visited, r)
for i in range(1, n+1):
    print(visited[i])

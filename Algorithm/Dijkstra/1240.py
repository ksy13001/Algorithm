from collections import deque
import heapq
INF = int(1e9)


def dijkstra(start, end):
    q = []
    distance = [INF] * (n+1)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for next_node, next_dist in graph[now]:
            cost = dist + next_dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance[end]


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
target = []
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
for _ in range(m):
    a, b = map(int, input().split())
    print(dijkstra(a, b))

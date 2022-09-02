import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
result = 0

def dijkstra(start):
    global distance
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(x)
r = distance


for i in range(1, n+1):
    dijkstra(i)
    result = max(distance[x] + r[i], result)

print(result)

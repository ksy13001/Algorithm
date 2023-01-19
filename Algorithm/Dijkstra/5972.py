import heapq
INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]


def dijkstra():
    q = []
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    while q:
        d, node = heapq.heappop(q)
        if distance[node] < d:
            continue
        for i in graph[node]:
            cost = d + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))



for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra()
print(distance[n])

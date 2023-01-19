import sys, heapq
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
distance = [INF for _ in range(n+1)]
route = [INF for _ in range(n+1)]


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next_n, next_d in graph[node]:
            cost = dist + next_d
            if cost < distance[next_n]:
                route[next_n] = node
                distance[next_n] = cost
                heapq.heappush(q, (cost, next_n))


for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
dijkstra()
print(n-1)
for i in range(2, n+1):
    print(i, route[i])

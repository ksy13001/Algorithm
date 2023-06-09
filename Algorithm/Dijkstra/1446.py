import heapq, sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dis, now = heapq.heappop(q)
        if dis > distance[now]:
            continue
        for next_node, next_dis in graph[now]:
            cost = next_dis + dis
            if distance[next_node] > cost:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))


n, d = map(int, input().split())
graph = [[]for _ in range(d+1)]
distance = [INF] * (d+1)
for i in range(d):
    graph[i].append((i+1, 1))
for _ in range(n):
    a, b, c = map(int, input().split())
    if b <= d:
        graph[a].append((b, c))
dijkstra(0)
print(distance[d])

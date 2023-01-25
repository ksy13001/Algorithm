import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize #int(1e9) 사용 x
n, p, k = map(int, input().split())
graph = [[]for _ in range(n+1)]
distance = [[INF for _ in range(k+1)]for _ in range(n+1)]
for _ in range(p):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra():
    q = []
    heapq.heappush(q, (0, 1, 0))
    distance[1][0] = 0
    while q:
        dist, now, cnt = heapq.heappop(q)
        if distance[now][cnt] < dist:
            continue
        for n_node, n_dist in graph[now]:
            cost = n_dist + dist
            if cost < distance[n_node][cnt]:
                distance[n_node][cnt] = cost
                heapq.heappush(q, (cost, n_node, cnt))
            if cnt < k and dist < distance[n_node][cnt+1]:
                distance[n_node][cnt+1] = dist
                heapq.heappush(q, (dist, n_node, cnt+1))


dijkstra()
print(min(distance[n]))


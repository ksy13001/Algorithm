import sys, heapq
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist < distance[now]:
            continue
        for next_node, next_dist in graph[now]:
            cost = next_dist + dist
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(q, (cost, next_node))
    return distance


for i in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split()) # g, h 사이 교차로 지나감
    graph = [[] for _ in range(n+1)]
    target = []
    ans = []
    x, y, l = 0, 0, 0
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    d = dijkstra(s)
    arr_g = dijkstra(g)
    arr_h = dijkstra(h)
    for _ in range(t):
        k = int(input())
        target.append(k)
        if d[g]+arr_g[h] + arr_h[k] == d[k]:
            ans.append(k)
        elif d[h]+arr_h[g] + arr_g[k] == d[k]:
            ans.append(k)
    print(*sorted(ans))

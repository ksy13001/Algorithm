import heapq
import sys
INF = int(1e9)
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[]for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, target = map(int, input().split())
distance = [INF] * (n + 1)
route = [start] * (n + 1)


def dijkstra(start):
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
                route[i[0]] = now
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
result = []
temp = target
while temp != start:
    result.append(temp)
    temp = route[temp]    
result.append(start)
result.reverse()


print(distance[target])
print(len(result))
print(*result)

import sys
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []


def bf(start):
    global distance
    distance = [INF] * (n+1)
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            now_node, next_node, cost = graph[j]
            if distance[now_node] != INF and distance[next_node] > distance[now_node] + cost:
                distance[next_node] = distance[now_node] + cost
                if i == n-1:
                    return False
    return True


for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))

if not bf(1):
    print(-1)
else:
    for i in range(2, n+1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print(-1)

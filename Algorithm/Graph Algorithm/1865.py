import sys
input = sys.stdin.readline
INF = int(1e9)


def bf(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    for i in range(n):
        for j in graph:
            now_node, next_node, cost = j
            if distance[now_node] + cost < distance[next_node]:
                distance[next_node] = distance[now_node] + cost
                if i == n-1:
                    return False
    return True


for i in range(int(input())):
    graph = []
    n, m, w = map(int, input().split())
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))

    ans = 'NO'
    if not bf(1):
        ans = 'YES'
    print(ans)

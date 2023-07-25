import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
# 아직 방문하지 않은 도시들을 거쳐 시작점으로 돌아오는데 드는 최소 비용
dp = {} # (현재위치(now), 방문한 도시(visited))


def dfs(now, visited):
    # visited -> 비트 마스킹으로 표시 / 방문한 도시 -> 1, 방문하지 않은 도시 -> 0
    if visited == (1 << n) - 1:
        if graph[now][0]: # 출발지로 돌아올 수 있으면
            return graph[now][0]
        else:
            return INF
    if (now, visited) in dp:    # 이미 최소비용이 존재 할 때
        return dp[(now, visited)]
    min_cost = INF
    for nc in range(1, n):
        if graph[now][nc] == 0 or visited & (1 << nc): # 가는 길이 없거나 방문한 경우
            continue
        # (visited | (1<<nc)) -> visited 에 방문할 도시 1 표시
        min_cost = min(min_cost, dfs(nc, visited|(1<<nc)) + graph[now][nc])
    dp[(now, visited)] = min_cost
    return min_cost


print(dfs(0, 1))

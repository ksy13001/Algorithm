import sys
input = sys.stdin.readline
INF = int(1e9)
sys.setrecursionlimit(10**7)
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
# 아직 방문하지 않은 도시들을 거쳐 시작점으로 돌아오는데 드는 최소 비용
dp = {}  # (현재위치(now), 방문한 도시(visited))
"""
ex) 현재 위치 1, 방문 기록 0011(2) -> 0, 1 방문       dp[1][0011] = dp[1][3]
    현재 위치 2, 방문 기록 0111(2) -> 0, 1, 2 방문    dp[2][0111] = dp[2][7]
    2 -> 3 으로 이동 : dp[2][visited] + graph[2][3] # graph[2][3] : 2 -> 3 으로 이동할 때 비용
    dp[3][1111] = dp[2][7] + graph[2][3]
"""


# visited -> 비트 마스킹으로 표시 / 방문한 도시 -> 1, 방문하지 않은 도시 -> 0
def dfs(now, visited):
    # 모두 방문 했을 경우 -> 시작점 으로 돌아 와야함
    if visited == (1 << n) - 1:
        # 현재 지점에서 시작점 까지 가는 길이 있는 경우 (문제에서 길이 없을 수도 있다함)
        if graph[now][0]:
            return graph[now][0]
        else:
            return INF
    # 이미 최소 비용 경로가 있을 경우
    if (now, visited) in dp:
        return dp[(now, visited)]
    min_cost = INF
    for next_city in range(1, n):
        # 현재 지점에서 다음 지점으로 가는 길이 없을 경우
        if graph[now][next_city] == 0:
            continue
        # 다음 지점을 이미 방문 했을 경우
        if visited & (1 << next_city) != 0:
            continue
        # (visited | (1<<nc)) -> visited 에 방문할 도시 1 표시
        min_cost = min(min_cost, dfs(next_city, visited | (1 << next_city)) + graph[now][next_city])
    dp[(now, visited)] = min_cost
    return min_cost


print(dfs(0, 1))




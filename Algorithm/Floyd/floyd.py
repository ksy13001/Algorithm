import sys
INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[INF]*(n + 1)for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

#현재 선택된 노드 k
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("INF", end=' ')
        else:
            print(graph[i][j],end=' ')
    print()

"""
    Dab = min(Dab, Dak + Dkb)
    단계마다 거쳐가는 노드 기준으로 실행, 현재 노드를 거쳐가는 모든 경우를 고려함
    2차원 리스트에 최단거리 정보 저장
    현재 확인하는 노드를 제외하고 (n-1)개의 노드 중에서  서로 다른 노드쌍 (a, b) 선택
    a -> 현재노드 -> b 로 가는 비용 확인 후 최단거리 갱신
    
    1. graph[a][b] = c, 자기 자신 노드(i==j) 거리 0으로 초기화
    2. 3중 반복문 사용
    3. 값이 INF인 경우 고려해서 출력
"""

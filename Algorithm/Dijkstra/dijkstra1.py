import sys
input = sys.stdin.readline
#무한대
INF = int(1e9)
#노드의 개수, 간선의 개수
n, m = map(int, input().split())
#시작점
start = int(input())
#연결된 노드와 노드와의 간선값을 나타내는 리스트
graph = [[]for i in range(n+1)]
#방문확인리스트
visited = [False]*(n+1)
#최단거리 테이블 초기화
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


#방문하지않은 노드중 최단거리 노드 번호 반환
def get_smallest_node():
    min_node = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_node and not visited[i]:
            min_node = distance[i]
            index = i
    return index


def dijkstra(start):
    #시작노드 거리 0
    distance[start] = 0
    visited[start] = True
    #노드1에 연결된 노드들의 거리
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        #최단거리 노드 인덱스 now
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)
for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

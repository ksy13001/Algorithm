import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
#n = 노드의 개수, m = 간선의 개수
n, m = map(int, input().split())
start = int(input())

graph = [[]for i in range(n+1)]
#최단거리 테이블
distance = [INF] * (n + 1)

#간선 값 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    #양방향이고 값이 같을때
    #graph[b].append((a, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))   #(거리, 노드) 순으로 넣는 이유 : 힙큐에서는 첫번째 요소에 따라 정렬, 우리는 거리순으로 정렬해야 하기 때문
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        #이미 방문한 노드인 경우
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # i[1] -> graph 에서 거리이기 때문
            cost = dist + i[1]
            print("주변노드 거리 + 현재최소거리 : ", cost)
            #cost 가 최소거리 테이블 값보다 작을경우 푸시
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)


for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

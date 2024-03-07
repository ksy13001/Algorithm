from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [[]for _ in range(n+1)]

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    if len(arr) > 1:
        graph[i] = arr[:-1]

m = int(input())
first = list(map(int, input().split()))

near_rumor = [0 for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in first:
    visited[i] = 1
q = deque(first)
while q:
    now = q.popleft()
    spread = []
    for next_node in graph[now]:
        if visited[next_node] == 0:
            near_rumor[next_node] += 1
            if near_rumor[next_node] >= len(graph[next_node])/2:
                spread.append(next_node)
    for i in spread:
        visited[i] = visited[now] + 1
        q.append(i)
for i in range(1, n+1):
    print(visited[i]-1, end=' ')

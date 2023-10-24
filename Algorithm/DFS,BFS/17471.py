import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
num = [0] + list(map(int, input().split()))
total = sum(num)
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    arr = list(map(int, input().split()))
    graph[i] = arr[1:]


def bfs(arr):
    start = arr[0]
    q = deque([start])
    visited = [start]
    while q:
        now = q.popleft()
        for i in graph[now]:
            if i not in visited and i in arr:
                q.append(i)
                visited.append(i)
    return visited


ans = INF
for i in range(1, n//2 + 1):
    arr = list(combinations(range(1, n+1), i))
    for com in arr:
        v0 = bfs(com)
        arr1 = [i for i in range(1, n+1) if i not in com]
        v1 = bfs(arr1)
        """
        print(com, arr1)
        print('v0:',v0)
        print('v1:',v1)
        """
        if len(v0) + len(v1) == n:
            a0, a1 = 0, 0
            for i in v0:
                a0 += num[i]
            for j in v1:
                a1 += num[j]
            ans = min(ans, abs(a1-a0))
if ans == INF:
    print(-1)
else:
    print(ans)

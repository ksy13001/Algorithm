from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[]]
for _ in range(n):
    graph.append(list(map(int, input().split())))
target = list(map(int, input().split()))


def bfs(start, end):
    q = deque([start])
    visited = [False for _ in range(n+1)]
    while q:
        now = q.popleft()
        for next_idx, con in enumerate(graph[now]):
            if con and next_idx+1 != now and not visited[next_idx+1]:
                if next_idx+1 == end:
                    return True
                q.append((next_idx+1))
                visited[next_idx+1] = True
    return False


def sol():
    if len(set(target)) == 1:
        print("YES")
        return
    for i in range(m-1):
        if not bfs(target[i], target[i+1]):
            print('NO')
            return
    print('YES')


sol()
"""
4
4
0 1 0 0
1 0 1 0
0 0 0 1
1 0 0 0
1 4 1 4
"""

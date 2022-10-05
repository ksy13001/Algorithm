from collections import deque
n, k = map(int, input().split())
visited = [False] * 10000000


def bfs(n):
    cnt = 0
    q = deque()
    q.append((n, cnt))
    visited[n] = True
    while q:
        temp, cnt = q.popleft()
        if temp == k:
            return cnt
        for i in (temp + 1, temp - 1, temp * 2):
            if not visited[i] and 0 < i < 200001:
                q.append((i, cnt + 1))
                visited[i] = True


print(bfs(n))

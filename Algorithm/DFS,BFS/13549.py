from collections import deque
n, k = map(int, input().split())
visited = [False] * 100001


def bfs(n):
    cnt = 0
    q = deque()
    q.append((n, cnt))
    visited[n] = True
    while q:
        now, cnt = q.popleft()
        if now == k:
            return cnt
        for i in (now * 2, now + 1, now - 1):
            if 0 <= i < 100001:
                if not visited[i]:
                    if i == now * 2:
                        q.append((i, cnt))
                    else:
                        q.append((i, cnt + 1))
                    visited[i] = True


print(bfs(n))

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = list(range(1, 101))
visited = [False]*101
warp = {}
for _ in range(n+m):
    a, b = map(int, input().split())
    warp[a] = b


def bfs():
    q = deque([(1, 0)])
    visited[1] = True
    while q:
        now, cnt = q.popleft()
        if now == 100:
            return cnt
        for i in range(1, 7):
            next_ = now + i
            if 0 < next_ <= 100:
                if next_ in warp:
                    if not visited[warp[next_]]:
                        q.append((warp[next_], cnt + 1))
                        visited[warp[next_]] = True
                else:
                    if not visited[next_]:
                        q.append((next_, cnt + 1))
                        visited[next_] = True

print(bfs())

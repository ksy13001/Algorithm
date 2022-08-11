from collections import deque
n, cur, target, u, d = map(int, input().split())
building = [[]for _ in range(n+1)]
for f in range(1, n+1):
    if (f+u) <= n:
        building[f].append(f + u)
    if (f-d) > 0:
        building[f].append(f - d)
visited = [False]*(n+1)
cnt = 0


def bfs(v):
    global cnt
    que = deque()
    que.append(v)
    while que:
        now = que.popleft()
        if not visited[now]:
            if now == target:
                visited[now] = True
                return cnt
                break
            if len(building[now]) != 0:
                if now < target:
                    que.append(max(building[now]))
                elif now > target:
                    que.append(min(building[now]))
            cnt += 1
            visited[now] = True
    return "use the stairs"


print(bfs(cur))

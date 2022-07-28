from collections import deque

n = int(input())
tx, ty = map(int, input().split())
m = int(input())
fam = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    fam[a].append(b)
    fam[b].append(a)
visited = [False] * (n + 1)
cnt = 0


def bfs(per, target):
    global cnt
    que = deque()
    que.append((per, cnt))
    while que:
        now, count = que.popleft()
        if now == target:
            return count
        visited[now] = True
        for i in fam[now]:
            if not visited[i]:
                que.append((i, count + 1))
                visited[i] = True
    return -1


print(bfs(tx, ty))

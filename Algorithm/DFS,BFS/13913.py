from collections import deque
n, k = map(int, input().split())
visited = [-1]*100001


def bfs(n):
    route = [-1] * 100001
    result = []
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        now = q.popleft()
        if now == k:
            print(visited[now])
            temp = k
            for i in range(visited[now]):
                result.append(route[temp])
                temp = route[temp]
            result.reverse()
            print(*result, k)
        for i in (now * 2, now - 1, now + 1):
            if 0 <= i < 100001 and visited[i] == -1:
                visited[i] = visited[now] + 1
                route[i] = now
                q.append(i)


bfs(n)

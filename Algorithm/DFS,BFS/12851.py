from collections import deque
n, k = map(int, input().split())
visited = [-1] * 100001
cnt = 0


def bfs(n):
    global cnt
    visited[n] = 0
    q = deque()
    q.append(n)
    while q:
        temp = q.popleft()
        if temp == k:
            cnt += 1
        for i in (temp + 1, temp - 1, temp * 2):
            if 0 <= i < 100001:
                if visited[i] == -1 or (visited[i] >= visited[temp] + 1):
                    q.append(i)
                    visited[i] = visited[temp] + 1


bfs(n)
print(visited[k])
print(cnt)

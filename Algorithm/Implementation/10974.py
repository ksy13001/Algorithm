n = int(input())
ori = list(range(1, n+1))
visited = [False]*n


def per(arr):
    if len(arr) == n:
        print(*arr)
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            per(arr + [ori[i]])
            visited[i] = False

per([])

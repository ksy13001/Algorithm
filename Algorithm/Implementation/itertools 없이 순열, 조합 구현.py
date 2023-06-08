n = int(input())
ori = list(range(1, n+1))
visited = [False]*n


def per(arr, k):
    if len(arr) == k:
        print(*arr)
        return arr
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            per(arr + [ori[i]], k)
            visited[i] = False


def com(arr, idx, k):
    if len(arr) == k:
        print(*arr)
        return arr
    for i in range(idx+1, n):
        if not visited[i]:
            visited[i] = True
            com(arr + [ori[i]], i, k)
            visited[i] = False

per([], 2)
print()
com([], -1, 2)

t = 0
while True:
    t += 1
    n = int(input())
    if n == 0:
        break
    name = []
    for _ in range(n):
        name.append(input())
    visited = [0 for _ in range(n)]
    for _ in range(2*n-1):
        index, s = map(str, input().split())
        visited[int(index)-1] += 1
    for i in range(n):
        if visited[i] == 1:
            print(t, name[i])
            break

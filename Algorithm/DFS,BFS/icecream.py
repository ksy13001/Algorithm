from collections import deque

n, m = map(int, input().split())
ice =[]
for _ in range(n):
    ice.append(list(map(int,input())))
print(ice)
def dfs(x, y):
    if x >= n or y >= m or x < 0 or y < 0:
        return False
    if ice[x][y] == 1:
        return False

    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False
result=0

for x in range(n):
    for y in range(m):
        if dfs(x, y)==True:
            result+=1
print(result)

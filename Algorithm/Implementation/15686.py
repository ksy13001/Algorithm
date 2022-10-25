import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
INF = int(1e9)
for _ in range(n):
    graph.append(list(map(int, input().split())))
chicken = []
house = []
target = []
result = []
visited = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i, j))
        elif graph[i][j] == 1:
            house.append((i, j))


def choose(cnt):
    if cnt == m:
        get_distance()
        return
    for i, (x, y) in enumerate(chicken):
        if not visited[x][y]:
            #조합중 중복된거 배제 
            if target:
                if i < target[-1][0]:
                    continue
            target.append((i, (x, y)))
            visited[x][y] = True
            choose(cnt + 1)
            target.pop()
            visited[x][y] = False


def get_distance():
    chicken_distance = 0
    print(target)
    for hx, hy in house:
        temp = INF
        for i, (cx, cy) in target:
            temp = min(abs(hx - cx) + abs(hy - cy), temp)
            if temp == 1:
                break
        chicken_distance += temp
    result.append(chicken_distance)


choose(0)
print(min(result))

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(str, input())))
w, h = 0, 0
# 가로
for i in range(n):
    cnt1, cnt2 = 0, 0
    for j in range(n):
        if graph[i][j] == '.':
            cnt1 += 1
        else:
            cnt1 = 0
        if cnt1 == 2:
            w += 1
        if graph[j][i] == '.':
            cnt2 += 1
        else:
            cnt2 = 0
        if cnt2 == 2:
            h += 1


print(w, h)

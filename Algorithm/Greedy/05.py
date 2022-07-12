n, m = map(int, input().split())
weight = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i, n):
        if weight[j] != weight[i]:
            cnt += 1
print(cnt)

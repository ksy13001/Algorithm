n = int(input())
arr = list(map(int, input().split()))
'''
10
1 5 2 1 4 3 4 5 2 1
'''
up = [1] * n
down = [1] * n
arr2 = list(reversed(arr))

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            up[i] = max(up[i], up[j] + 1)
for i in range(1, n):
    for j in range(0, i):
        if arr2[j] < arr2[i]:
            down[i] = max(down[i], down[j] + 1)
down.reverse()
ans = 0
for i in range(n):
    ans = max(ans, up[i] + down[i])
print(ans-1)

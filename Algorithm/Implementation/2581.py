import math
m = int(input())
n = int(input())

arr = [True for _ in range(n+1)]


for i in range(2, int(math.sqrt(n))+1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i*j] = False
            j += 1

ans = []
for i in range(m, n+1):
    if arr[i]:
        ans.append(i)
if 1 in ans:
    ans.remove(1)
if ans:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)

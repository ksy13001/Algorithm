import math
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x, y = 1, 1
for i in range(n):
    x *= a[i]
for j in range(m):
    y *= b[j]
ans = str(math.gcd(x, y))
print(ans[-9:])

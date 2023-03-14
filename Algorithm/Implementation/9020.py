import math
t = int(input())
arr = [True] * (10001)
arr[0], arr[1] = False, False
for i in range(2, int(math.sqrt(10000))+1):
    if arr[i]:
        j = 2
        while i * j <= 10000:
            arr[i*j] = False
            j += 1


for _ in range(t):
    n = int(input())
    for i in range(n//2, n):
        if arr[n-i] and arr[n - (n-i)]:
            print(n-i, n-(n-i))
            break

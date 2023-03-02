import math
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = False
    for i in range(n-1):
        if not ans:
            for j in range(i+1, n):
                if math.gcd(arr[i], arr[j]) <= 2:
                    ans = True
    if ans:
        print("Yes")
    else:
        print("No")

t = int(input())

for _ in range(t):
    n = int(input())
    d = [0]*(n+3)
    d[1] = 1
    d[2] = 2
    d[3] = 4
    for i in range(4, n+1):
        d[i] = d[i-1] + d[i-2] + d[i-3]
    print(d[n])

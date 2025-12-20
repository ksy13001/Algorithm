t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    total_power = 0
    total_weight = 0
    for _ in range(n):
        w, p = map(int, input().split())
        arr.append((w, p, w+p))
        total_weight += w
        total_power += p
    arr.sort(key= lambda x:-x[2])
    now_power = 0
    ans = 0
    for i in range(len(arr)):
        w, p, cost = arr[i]
        now_power += p
        total_weight -= w
        if now_power >= total_weight:
            ans = len(arr) - i - 1
            break
    print(ans)

n, t = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
closed_time = 0
for mc in arr:
    if closed_time <= mc:
        closed = False
    if not closed and closed_time <= mc:
        ans += mc - closed_time
        closed = True
        closed_time = mc + 100
print(ans + max(0, t-closed_time))
# 100 150 300 350 700
# 0~100, 200~300 400~700 = 100 + 100 + 300 = 500

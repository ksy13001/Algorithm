import sys
input = sys.stdin.readline
n, m = map(int, input().split())
money = []
for _ in range(n):
    money.append(int(input()))
start = max(money)
end = sum(money)
ans = sys.maxsize
while start <= end:
    mid = (start + end) // 2
    k = mid
    cnt = 1
    for now in money:
        if k < now:
            cnt += 1
            k = mid
        k -= now
    if cnt > m or mid < max(money):
        start = mid + 1
    else:
        end = mid - 1
        ans = mid
print(ans)

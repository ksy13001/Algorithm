import sys
input = sys.stdin.readline
n, m = map(int, input().split())
gate = []
for _ in range(n):
    gate.append(int(input()))

start = min(gate)
end = max(gate) * m
ans = end
while start <= end:
    people = 0
    mid = (start + end) // 2
    for i in gate:
        people += mid // i
    if people < m:
        start = mid + 1
    else:
        end = mid - 1
        ans = min(ans, mid)
print(ans)

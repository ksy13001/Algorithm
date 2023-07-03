# 52.3
# 146 523 229
n, x, y, z = map(int, input().split())

start = 0
end = max(x, y, z)
ans = 0
for _ in range(100):
    mid = (start + end)/2
    print(start, end, mid)
    k = (x//mid) * (y//mid) * (z//mid)  # a 상자 개수
    # a 작을수록 상자 개수 늘어남
    # 소수점 포함하기 때문에 mid + 1, mid - 1 x
    if k < n:
        end = mid
    else:
        start = mid
print(end)

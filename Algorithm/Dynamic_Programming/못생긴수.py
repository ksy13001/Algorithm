n = int(input())
dp = [0]*n
dp[0] = 1
# 2, 3, 5배 인덱스
i2, i3, i5 = 0, 0, 0
# 곱셈값 S
e2, e3, e5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(e2, e3, e5)
    if dp[i] == e2:
        i2 += 1
        e2 = dp[i2] * 2
    # elif 사용시 중복 발생
    if dp[i] == e3:
        i3 += 1
        e3 = dp[i3] * 3
    if dp[i] == e5:
        i5 += 1
        e5 = dp[i5] * 5
print(dp[n-1])

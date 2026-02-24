def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    dp = [0] * (n+1)
    for i, num in enumerate(arr):
        dp[i+1] = max(dp[i] + num, num)
    print(max(dp[1:]))


for _ in range(int(input())):
    solution()

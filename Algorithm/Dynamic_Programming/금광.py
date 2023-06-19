"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
"""
19
16
"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    k = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(k[i*m:(i+1)*m])  # 0-3, 4-7, 8-11
    dp = [[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        dp[i][0] = arr[i][0]
    for j in range(1, m): 
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j - 1]) + arr[i][j]
            elif i == n-1:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1]) + arr[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1]) + arr[i][j]
    ans = 0
    for k in range(n):
        ans = max(ans, dp[k][m-1])
    print(ans)

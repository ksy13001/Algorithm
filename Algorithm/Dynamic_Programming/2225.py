# dp 문제는 일단 점화식 부터
# 직접 구현 해보며 규칙 찾기
def solve(n, k):
    dp = [[0 for _ in range(n)] for _ in range(k)]
    for i in range(n):
        dp[0][i] = 1
    for j in range(k):
        dp[j][0] = j+1

    for i in range(1, k):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    #for i in range(k):    print(dp[i])
    print(dp[k-1][n-1]%1000000000)


n, k = map(int, input().split())
solve(n, k)

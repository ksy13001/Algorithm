import sys, heapq
#input = sys.stdin.readline

dp = [0] * 46
dp[0] = 0
dp[1] = 1


for i in range(2, 46):
    dp[i] = dp[i-1] + dp[i-2]
dp.reverse()


def sol():
    n = int(input())
    ans = []
    for i in range(50):
        if dp[i] <= n:
            n -= dp[i]
            ans.append(dp[i])
            if n == 0:
                ans.sort()
                print(*ans)
                return
    return -1


for _ in range(int(input())):
    sol()

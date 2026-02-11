# https://atcoder.jp/contests/awc0003/tasks/awc0003_d
n, k, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

ans = 0
start = 0
for end in range(k, n+1):
    ans += start
    while end - start >= k and prefix_sum[end] - prefix_sum[start] >= m:
        ans += 1
        start += 1
print(ans)

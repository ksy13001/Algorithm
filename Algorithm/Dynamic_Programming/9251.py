arr1 = list(input())
arr2 = list(input())
dp = [0 for _ in range(len(arr2))]
for i in range(len(arr1)):
    cnt = 0
    for j in range(len(arr2)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif arr1[i] == arr2[j]:
            dp[j] = cnt + 1
print(max(dp))

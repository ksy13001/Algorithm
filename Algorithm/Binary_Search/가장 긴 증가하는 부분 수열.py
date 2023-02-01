import sys
import bisect
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [arr[0]]


for i in range(n):
    if arr[i] > ans[-1]:
        ans.append(arr[i])
    else:
        index = bisect.bisect_left(ans, arr[i])
        ans[index] = arr[i]
        
print(ans)

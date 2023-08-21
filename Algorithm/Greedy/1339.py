import sys
input = sys.stdin.readline
n = int(input())
arr = []
dic = {}

for _ in range(n):
    arr.append(list(input().rstrip()))

num = []
for i in range(n):
    k = len(arr[i])
    for j in range(k):
        if arr[i][j] not in dic:
            dic[arr[i][j]] = 10 ** (k-j-1)
        else:
            dic[arr[i][j]] += 10 ** (k-j-1)

num = list(dic.values())
num.sort(reverse=True)
cnt = 9
ans = 0
for i in num:
    ans += i * cnt
    cnt -= 1
print(ans)

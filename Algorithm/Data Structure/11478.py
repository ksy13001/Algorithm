s = input()
n = len(s)
ans = set()
for i in range(1, n+1):
    for j in range(n):
        if j+i == n+1:
            break
        ans.add(s[j:j+i])
print(len(ans))

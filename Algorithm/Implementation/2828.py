n, m = map(int, input().split())
apple = []
j = int(input())
for _ in range(j):
    apple.append(int(input()))
l = 1
r = 1 + m-1
ans = 0
for i in range(j):
    if l <= apple[i] <= r:
        continue
    elif apple[i] < l:
        ans += abs(l-apple[i])
        l = apple[i]
        r = l+m-1
    elif r < apple[i]:
        ans += abs(r - apple[i])
        r = apple[i]
        l = r-m+1
print(ans)

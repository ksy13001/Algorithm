n = int(input())
ans = 10000000
for i in range(n//5 + 1):
    cnt = 0
    cnt += i
    if (n-5*i) % 2 == 0:
        cnt += (n-5*i)//2
        ans = min(cnt, ans)
if ans == 10000000:
    print(-1)
else:
    print(ans)

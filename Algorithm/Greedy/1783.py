n, m = map(int, input().split())
ans = 1
if n == 1:
    ans = 1
elif n > 2 and m > 6:
    ans = m - 2
elif n == 2:
    ans = (m+1)//2
    if ans > 4:
        ans = 4
# n > 2
elif m <= 4:
    ans = m
elif m > 4:
    ans = 4

print(ans)

n = int(input())
cnt = 0
stick = [64, 32, 16, 8, 4, 2, 1]
for i in stick:
    if n - i >= 0:
        n -= i
        cnt += 1
    if n == 0:
        break
print(cnt)

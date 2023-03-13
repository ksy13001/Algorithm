n = int(input())
now = 1
while now < n:
    n -= now
    now += 1


if now % 2 == 0:
    up = n
else:
    up = now - n + 1
print(f'{up}/{now-up+1}')

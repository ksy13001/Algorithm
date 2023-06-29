n = int(input())

now = 0
cnt = 1
start = 1
end = 2
now = start+end
while start < end < n:
    if now < n:
        end += 1
        now += end
    elif now > n:A
        now -= start
        start += 1
    else:
        cnt += 1
        end += 1
        now += end
print(cnt)

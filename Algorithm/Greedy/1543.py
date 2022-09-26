origin = input()
target = input()
n = 0
cnt = 0
while n <= len(origin) - len(target):
    if origin[n:n + len(target)] == target:
        cnt += 1
        n += len(target)
    else:
        n += 1
print(cnt)

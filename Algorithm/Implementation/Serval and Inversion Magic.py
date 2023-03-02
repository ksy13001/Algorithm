import sys
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, str(input())))
    cnt = 0
    ans = True
    for i in range(n//2):
        if arr[i] != arr[-(i+1)]:
            if cnt == 0:
                cnt += 1
            elif cnt == 2:
                cnt += 1
        else:
            if cnt == 1:
                cnt += 1
        if cnt == 3:
            ans = False
            continue
    if ans:
        print('YES')
    else:
        print('NO')

n = int(input())
cnt = 0
while True:
    arr = list(map(int, str(n)))
    if len(arr) == 1:
        print(cnt)
        if arr[0] % 3 == 0:
            print('YES')
        else:
            print('NO')
        break
    n = sum(arr)
    cnt += 1

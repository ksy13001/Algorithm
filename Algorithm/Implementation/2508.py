
for _ in range(int(input())):
    input()
    n, m = map(int, input().split())
    arr = []
    cnt = 0
    for _ in range(n):
        arr.append(list(input()))
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'o':
                # 위 아래 확인
                if i - 1 >= 0 and i + 1 < n:
                    if arr[i-1][j] == 'v' and arr[i+1][j] == '^':
                        cnt += 1
                # 좌 우 확인
                if j - 1 >= 0 and j + 1 < m:
                    if arr[i][j-1] == '>' and arr[i][j+1] == '<':
                        cnt += 1
    print(cnt)

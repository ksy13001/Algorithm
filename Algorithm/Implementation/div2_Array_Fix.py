def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            a, b = arr[i-1]//10, arr[i-1]%10
            if a > b:
                return print('NO')
            if b <= arr[i]:
                arr[i-1] = a
            else:
                return print('NO')
    return print('YES')



for _ in range(int(input())):
    sol()

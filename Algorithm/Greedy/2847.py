import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))
    ans = 0
    for i in range(n-1, 0, -1):
        if arr[i] <= arr[i-1]:
            ans += arr[i-1] - (arr[i]-1)
            arr[i-1] = arr[i]-1
    print(ans)



sol()

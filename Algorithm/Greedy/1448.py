import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    arr.sort(reverse=True)
    for i in range(n-2):
        if arr[i] < arr[i+1] + arr[i+2]:
            print(arr[i] + arr[i+1] + arr[i+2])
            return
    print(-1)
    return


sol()

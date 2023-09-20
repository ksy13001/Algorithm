import heapq


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = arr[-1]
    for i in range(n-1):
        ans += arr[i]/2
    print(ans)


sol()

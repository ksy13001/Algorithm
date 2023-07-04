import sys
input = sys.stdin.readline
def up(n):
    if n - int(n) >= 0.5:
        return int(n)+1
    else:
        return int(n)


def sol():
    n = int(input())
    if n == 0:
        print(0)
        return
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    k = up(n * 0.15)
    print(up(sum(arr[k:n-k])/(n-k*2)))
    return
sol()

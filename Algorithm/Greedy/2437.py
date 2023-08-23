import sys
input = sys.stdin.readline
# 저울의 추 ex) sum(i ~ i+3)+1 < arr(i+4) -> arr(i+4) 만들수 없음


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    if arr[0] > 1:
        print(1)
        return
    for i in range(n-1):
        if arr[i+1] > sum(arr[:(i+1)])+1:
            print(sum(arr[:(i+1)])+1)
            return
    print(sum(arr)+1)
    return


sol()

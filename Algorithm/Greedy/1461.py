import sys
INF = sys.maxsize
input = sys.stdin.readline


def sol():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    left = []
    right = []
    walk = 0
    for i in range(n):
        if arr[i] < 0:
            left.append(arr[i])
        else:
            right = arr[i:]
            break
    if left and right:
        # 양수길이가 더 길때
        if abs(left[0]) < right[-1]:
            for i in range(0, len(left), m):
                walk += abs(left[i]) * 2
            for i in range(len(right)-m-1, -1, -m):
                walk += right[i]*2
            walk += right[-1]
        # 음수 길이가 더 길때
        else:
            for i in range(len(right)-1, -1, -m):
                walk += right[i] * 2
            for i in range(0, len(left), m):
                walk += abs(left[i]) * 2
            walk += left[0]
    elif left:
        for i in range(0, len(left), m):
            walk += abs(left[i]) * 2
        walk += left[0]
    elif right:
        for i in range(len(right) - m - 1, -1, -m):
            walk += right[i] * 2
        walk += right[-1]
    print(walk)
sol()

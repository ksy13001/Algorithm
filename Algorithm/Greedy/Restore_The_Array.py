import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    change = -1
    for i in range(1, n-1):
        if arr[i] > arr[i-1]:
            if change == -1:
                arr.insert(i, 0)
                change = i
    if change == -1:
        arr.append(arr[-1])
    else:
        for i in range(change+1, n):
            if arr[i] < arr[i-1]:
                arr[i-1] = arr[i]
    print(*arr)
"""
11
5
3 4 4 5
4
2 2 1
5
0 0 0 0
6
0 3 4 4 3
2
10
4
3 3 3
5
4 2 5 5
4
3 3 3
4
2 1 0
3
4 4
6
8 1 3 5 10

"""

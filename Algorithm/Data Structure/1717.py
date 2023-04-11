import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
arr = list(range(n+1))


def find(i):
    if arr[i] != i:
        arr[i] = find(arr[i])
    return arr[i]


def union(a, b):
    fa, fb = find(a), find(b)
    if fa > fb:
        arr[fa] = fb
    elif fb > fa:
        arr[fb] = fa


for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')



import sys, math
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    k = 0
    for i in range(n):
        if arr[i] != i+1:
            k = math.gcd(k, abs(arr[i]-(i+1)))
    print(k)
# 주어진 배열이 permutation 인 경우, arr.index() 보다는 그냥 인덱스와 배열 값 활용
"""
7
3
3 1 2
4
3 4 1 2
7
4 2 6 7 5 3 1
9
1 6 7 4 9 2 3 8 5
6
1 5 3 4 2 6
10
3 10 5 2 9 6 7 8 1 4
11
1 11 6 4 8 3 7 5 9 10 2
"""

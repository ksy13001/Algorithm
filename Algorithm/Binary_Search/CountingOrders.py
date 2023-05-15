import sys
from bisect import bisect_left
input = sys.stdin.readline
mod = int(1e9) + 7
 
 
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = 1
    for i in range(n):
        cnt = bisect_left(b, a[i]) - i  # bisect 는 항상 오름차순 정렬된 배열에서만
        ans *= cnt
        ans %=mod
    print(ans)

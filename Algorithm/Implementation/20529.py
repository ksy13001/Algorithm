from itertools import combinations
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(str, input().split()))
    if n > 32:
        print(0)
    else:
        ans = 5 * n
        if len(set(arr)) == 1:
            print(0)
        else:
            for s1, s2, s3 in combinations(arr, 3):
                ans = min(ans, len(set(s1)-set(s2)) + len(set(s2)-set(s3)) + len(set(s3)-set(s1)))
            print(ans)

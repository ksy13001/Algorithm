import sys
INF = sys.maxsize
input = sys.stdin.readline
"""
9
SLLLLSSLL

7
"""


def sol():
    n = int(input().rstrip())
    arr = list(input().rstrip())
    if 'L' in arr:
        couple = arr.count('L')
        print(n - (couple//2) +1)
    else:
        print(n)
    return


sol()

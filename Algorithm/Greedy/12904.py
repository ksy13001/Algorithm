import sys
from collections import deque
input = sys.stdin.readline


def sol():
    a = list(input().rstrip())
    b = list(input().rstrip())
    while len(b) > len(a):
        if b[-1] == 'A':
            b.pop()
        else:
            b.pop()
            b.reverse()
    if a == b:
        print(1)
    else:
        print(0)
    return


sol()


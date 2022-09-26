import sys
from math import factorial
input = sys.stdin.readline
n = int(input())

cnt = 0

for x in str(factorial(n))[::-1]:
    if x == '0':
        cnt += 1
    else:
        print(cnt)
        break

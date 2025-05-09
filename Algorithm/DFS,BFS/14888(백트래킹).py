import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = int(1e9)
max_value = int(-1e9)


def solution(i, now):
    global add, sub, mul, div, min_value, max_value

    if i == n:
        max_value = max(max_value, now)
        min_value = min(min_value, now)
        return
    else:
        if add > 0:
            add -= 1
            solution(i + 1, now + num[i])
            add += 1
        if sub > 0:
            sub -= 1
            solution(i + 1, now - num[i])
            sub += 1
        if mul > 0:
            mul -= 1
            solution(i + 1, now * num[i])
            mul += 1
        if div > 0:
            div -= 1
            solution(i + 1, int(now/num[i]))
            div += 1


solution(1, num[0])
print(max_value)
print(min_value)


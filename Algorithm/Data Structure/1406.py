from collections import deque
import sys
input = sys.stdin.readline
arr = list(input().strip())
n = int(input())
cur = len(arr)
ls = deque(arr)
rs = deque([])


for _ in range(n):
    s = input().strip()
    if s == 'L':
        if ls:
            rs.appendleft(ls.pop())
    elif s == 'D':
        if rs:
            ls.append(rs.popleft())
    elif s == 'B':
        if ls:
            ls.pop()
    else:
        s, st = map(str, s.split())
        ls.append(st)
print(''.join(ls+rs))

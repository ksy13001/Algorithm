from collections import deque
import sys
t = int(input())
for _ in range(t):
    st = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    error = False
    now = 0
    cnt = 0
    if n == 0:
        arr = deque()
    for s in st:
        if s == 'D':
            if arr:
                if cnt % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                error = True
                break
        else:
            cnt += 1
    if cnt % 2 == 1:
        arr.reverse()
    if error:
        print('error')
    else:
        print("["+",".join(arr)+"]")

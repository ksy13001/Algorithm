from collections import deque
n = int(input())
q = deque(zip(range(1, n+1), map(int, input().split())))
while q:
    now, val = q.popleft()
    print(now, end=' ')
    if not q:
        break
    if val > 0:
        for i in range(val-1):
            a = q.popleft()
            q.append(a)
    else:
        for i in range(-val):
            a = q.pop()
            q.appendleft(a)

import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
arr = deque(map(int, input().rstrip()))
ans = []
cnt = 0
while arr and cnt < k:
    now = arr.popleft()
    while ans and ans[-1] < now and cnt < k:
        ans.pop()
        cnt += 1
    ans.append(now)
if arr:
    ans += arr
if cnt < k:
    ans = ans[:n-k]
print(''.join(map(str, ans)))

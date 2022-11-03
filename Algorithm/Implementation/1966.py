from collections import deque
t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque()
    for i in range(len(arr)):
        q.append((arr[i], i))
    while True:
        max_num = max(q, key=lambda x: x[0])
        value, index = q.popleft()
        if value < max_num[0]:
            q.append((value, index))
        else:
            cnt += 1
            if index == m:
                print(cnt)
                break

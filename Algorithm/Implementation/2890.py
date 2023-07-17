import re

r, c = map(int, input().split())
line = []
for _ in range(r):
    a = input()
    line.append(a[1:-1])
line.sort()
ans = [0 for _ in range(10)]
rank = 0
now = -1
for i in range(r):
    cnt = 0
    # l = re.sub(r'[^0-9]', '', i)
    if len(set(line[i])) != 1:
        for j in range(c-2):
            if line[i][j] == '.':
                cnt += 1
            else:
                if now != cnt:
                    rank += 1
                now = cnt
                ans[int(line[i][j])] = rank
                break
for i in range(1, 10):
    print(ans[i])

n = int(input())
parr = []
marr = []
for i in range(n):
    a = int(input())
    if a > 0:
        parr.append(a)
    else:
        marr.append(a)
parr.sort(reverse=True)
marr.sort()
ans = 0
plus = False
if len(parr) % 2 == 1:
    if parr[-1] == 1:
        parr.append(0)
    else:
        parr.append(1)
        plus = True
if len(marr) % 2 == 1:
    marr.append(1)
for i in range(0, len(parr), 2):
    if parr[i] == 1 and (parr[i+1] == 1 or parr[i+1] == 0) or (parr[i] > 1 and parr[i+1] == 1 and not plus):
        ans += parr[i] + parr[i+1]
    else:
        ans += parr[i] * parr[i+1]
for i in range(0, len(marr), 2):
    ans += marr[i] * marr[i+1]
print(ans)

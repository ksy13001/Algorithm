u, n = map(int, input().split())
name = [[]for _ in range(u+1)]
dic = {}
value = [0] * (u+1)
for _ in range(n):
    a, b = map(str, input().split())
    if b not in dic:
        dic[b] = 1
    else:
        dic[b] += 1
    name[int(b)].append(a)
m = min(dic.values())
v = u
for key, val in dic.items():
    if val == m:
        v = min(v, int(key))
print(name[v][0], v)

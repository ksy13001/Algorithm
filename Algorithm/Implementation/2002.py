n = int(input())
in_ = {}
out = []
ans = 0
for i in range(1, 1+n):
    in_[input()] = i
now = 1
for _ in range(n):
    s = input()
    if in_[s] != now:
        out.append(in_[s])
        ans += 1
    else:
        while True:
            now += 1
            if now not in out:
                break
print(ans)

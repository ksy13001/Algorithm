"""
3
5
7
7
"""
def sol():
    n = int(input())
    num = []
    for _ in range(n):
        num.append(int(input()))
    cnt = 0
    while True:
        m = max(num)
        i = num.index(m)
        if i == 0:
            if m in num[1:]:
                return cnt+1
            else: return cnt
        else:
            num[i] -= 1
            num[0] += 1
            cnt += 1
print(sol())

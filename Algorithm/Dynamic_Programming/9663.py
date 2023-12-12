n = int(input())
row = [0] * n
ans = 0


def check(now):
    for i in range(now):
        if row[i] == row[now] or (abs(i-now) == abs(row[i]-row[now])):
            return False
    return True


def dfs(now):
    global ans
    if now == n:
        ans += 1
        return
    else:
        for i in range(n):
            row[now] = i
            if check(now):
                dfs(now+1)


dfs(0)
print(ans)

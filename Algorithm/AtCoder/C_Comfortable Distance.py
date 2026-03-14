import math
def solution():
    n, l, r = map(int, input().split())
    s = input()
    ans = 0
    dic = {}
    for i in range(l, r+1):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1
    for i in range(n):
        now = s[i]
        if now in dic:
            ans += dic[now]

        if i+r+1 < n:
            if s[i+r+1] not in dic:
                dic[s[i+r+1]] = 1
            else:
                dic[s[i+r+1]] += 1
        if i+l < n:
            if s[i+l] not in dic:
                dic[s[i+l]] = 1
            else:
                dic[s[i+l]] -= 1
    print(ans)


solution()

"""
7 9 5
2 4
1 3
2 1
2 1
1 3

63
27 36

"""

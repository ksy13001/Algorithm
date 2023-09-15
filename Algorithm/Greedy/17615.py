import sys, math
input = sys.stdin.readline
INF = sys.maxsize


def sol():
    n = int(input())
    st = list(input().rstrip())
    blue = st.count('B')
    red = n-blue
    r = st.count('R')
    left, right = 1, 1
    for i in range(1, n):
        if st[i] == st[0]:
            left += 1
        else:
            break
    for j in range(n-2, -1, -1):
        if st[j] == st[-1]:
            right += 1
        else:
            break
    ans = INF
    if st[0] == 'R':
        ans = min(red-left, blue)
    else:
        ans = min(blue-left, red)
    if st[-1] == 'R':
        ans = min(ans, red-right, blue)
    else:
        ans = min(ans, blue-right, red)
    print(ans)

sol()

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    st = input().strip()
    cnt = 1
    ans = 0
    for i in range(1, n):
        if st[i-1] == st[i]:
            cnt += 1
        else:
            cnt = 1
        ans = max(ans, cnt)
    print(ans+1)

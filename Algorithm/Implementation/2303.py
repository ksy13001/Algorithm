from itertools import combinations as com
def sol():
    n = int(input())
    ans = -1
    now = -1
    for i in range(1,n+1):
        arr = list(map(int, input().split()))
        arr = set(com(arr, 3))
        cnt = 0
        for a, b, c in arr:
            cnt = max(cnt, (a+b+c)%10)
        if now <= cnt:
            now = cnt
            ans = i
    print(ans)


sol()

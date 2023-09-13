import sys
input = sys.stdin.readline


def sol():
    l, r = input().split()
    cnt = 0
    ans = 0
    if len(l) != len(r):
        print(0)
    else:
        for i in range(len(l)):
            if l[i] == r[i]:
                if l[i] == '8':
                    cnt += 1
                    ans = cnt
            else:
                print(cnt)
                return
        print(ans)


sol()

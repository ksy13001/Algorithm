import sys, math
INF = sys.maxsize
input = sys.stdin.readline


def sol():
    n = int(input())
    crane = list(map(int, input().split()))
    m = int(input())
    box = list(map(int, input().split()))
    crane.sort(reverse=True)
    box.sort(reverse=True)
    if box[0] > crane[0]:
        print(-1)
        return
    else:
        cnt = 0
        ans = 0
        while cnt < m:
            ans += 1
            for ci in range(n):
                for bi in range(len(box)):
                    if crane[ci] >= box[bi]:
                        box.remove(box[bi])
                        cnt += 1
                        break
        print(ans)
    return


sol()

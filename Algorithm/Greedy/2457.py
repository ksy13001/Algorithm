import sys, heapq
input = sys.stdin.readline

# 3/1 ~ 11/30
def sol():
    n = int(input())
    arr = []
    for _ in range(n):
        sm, sd, em, ed = map(int, input().split())
        arr.append((sm*100 + sd, em*100 + ed))
    arr.sort()
    cnt = 0
    ns, nd = 0, 0
    ts, td = 0, 0
    for start, end in arr:
        # 시작점 지정
        if start <= 301:
            if ns == 0:
                cnt += 1
            if nd < end:
                ns = start
                nd = end
            if nd >= 1201:
                print(1)
                return
        else:
            if start <= nd:
                if end >= 1201:
                    print(cnt + 1)
                    return
                if ts == 0:
                    ts, td = start, end
                elif td < end:
                    ts, td = start, end
            else:
                # ns, nd 갱신
                cnt += 1
                ns, nd = ts, td
                ts, td = start, end
                if nd < ts:
                    print(0)
                    return
    if nd < 1131:
        if td >= 1201 and ts <= nd:
            print(cnt+1)
        else:
            print('0')
    else:
        print(cnt)
    return


sol()

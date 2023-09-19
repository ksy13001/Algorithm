import sys, heapq
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    target, now_oil = map(int, input().split())
    arr.append((target, 0))
    now_dis = 0
    if now_oil >= target:
        print(0)
        return
    arr.sort(key=lambda x: (x[0], -x[1]))
    q = []
    cnt = 0
    for next_dis, next_oil in arr:
        # 기름 부족하면 지나온 주유소에서 기름 충전
        while q and next_dis - now_dis > now_oil:
            no, nd = heapq.heappop(q)
            now_oil += -no
            cnt += 1
        if next_dis - now_dis > now_oil:
            print(-1)
            return
        heapq.heappush(q, (-next_oil, next_dis))
        now_oil -= next_dis - now_dis
        now_dis = next_dis
        if now_oil + now_dis >= target:
            print(cnt)
            return
    print(cnt)


sol()

import sys, math, heapq
input = sys.stdin.readline
INF = sys.maxsize


def sol():
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    arr.sort()
    q = []
    ans = 1
    for start, end in arr:
        if not q:
            heapq.heappush(q, end)
        else:
            # 현재 회의 시간 >= 다음 회의 시간 -> 회의실 추가
            # 회의 끝날 경우 다음 회의 push
            while q and q[0] <= start:
                heapq.heappop(q)
            heapq.heappush(q, end)
            ans = max(ans, len(q))
    print(ans)


sol()

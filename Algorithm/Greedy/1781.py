import sys, heapq
input = sys.stdin.readline
# 힙큐에 먼저 채우고 pop 이 아니라 반대로
# 힙큐에 채우면서 조건에 안맞으면 pop


def sol():
    n = int(input())
    arr = []
    q = []
    for _ in range(n):
        d, c = map(int, input().split())
        arr.append((d, c))
    arr.sort(key=lambda x:(x[0], -x[1]))
    for dl, cl in arr:
        # 일단 컵라면 heappush
        heapq.heappush(q, cl)
        # 데드라인 못맞출 경우 가장 작은값 pop
        if len(q) > dl:
            heapq.heappop(q), len(q)
    print(sum(q))



sol()

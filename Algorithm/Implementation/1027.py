import sys
INF = sys.maxsize


def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    if n == 1:
        print(0)
        return
    else:
        for now in range(n):
            cnt = 0
            gap = INF
            for left in range(now-1, -1, -1):
                # inc > 0 -> 앞 건물이 낮음 / inc < 0 -> 앞 건물이 높음
                inc = (arr[now] - arr[left]) / abs(now - left)  # 함부로 // 쓰지말기
                if inc < gap:
                    cnt += 1
                    gap = inc
            gap = INF
            for right in range(now+1, n):
                inc = (arr[now] - arr[right]) / abs(now - right)
                if inc < gap:
                    cnt += 1
                    gap = inc
            ans = max(ans, cnt)
        print(ans)

sol()

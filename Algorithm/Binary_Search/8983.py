import sys
input = sys.stdin.readline
m, n, l = map(int, input().split())
hunt = list(map(int, input().split()))
hunt.sort()
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
cnt = 0
for x, y in arr:
    start = 0
    end = m - 1
    while start <= end:
        mid = (start + end) // 2
        dist = abs(x - hunt[mid]) + y
        if dist > l:
            if hunt[mid] < x:
                start = mid + 1
            else:
                end = mid - 1
        else:
            cnt += 1
            break

print(cnt)

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip())))
ans = 1
pass_ = False
try:
    for i in range(n):
        for j in range(m):
            for k in range(1, min(n, m)):
                nx = i + k
                ny = j + k
                if nx < n and ny < m:
                    if arr[i][j] == arr[nx][j] == arr[i][ny] == arr[nx][ny]:
                        ans = max(ans, (k+1)**2)
                        if ans == min(n,m)**2:
                            raise NotImplementedError
except:
    ans = min(n,m)**2
print(ans)

import sys
input = sys.stdin.readline

n, a, b = map(int, input().split())
cnt = 0
while True:
    cnt += 1
    a = (a+1) // 2
    b = (b+1) // 2
    if a==b:
        print(cnt)
        break
else:
    print(-1)

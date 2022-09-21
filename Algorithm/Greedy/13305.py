import sys
input = sys.stdin.readline

n = int(input())
road = list(map(int, input().split()))  # 도로의 길이
oil = list(map(int, input().split()))  # 기름 값

now_oil = oil[0]
temp = now_oil * road[0]
for _next in range(1, n-1):
    if now_oil >= oil[_next]:
        now_oil = oil[_next]
    temp += now_oil * road[_next]
print(temp)

# 25 7 5
# 파이썬에서 소수점은 15까지
a, b, n = map(int, input().split())
for i in range(n+1):
    now = a//b
    a = (a%b)*10
print(now)

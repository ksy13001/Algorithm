def sol(a, b):
    k = 1
    for i in range(1, min(a, b)+1):
        if a % i == 0 and b % i == 0:
            k = max(k, i)
    p = a * b
    for i in range(p, max(a, b)-1, -1):
        if i % a == 0 and i % b == 0:
            p = min(p, i)
    print(p, k)


# 유클리드 호제법 사용
def GCM(a, b):
    if b > a:
        a, b = b, a
    while b:
        # a 나누기 b 가 딱 떨어질 때까지 나누기
        a, b = b, a%b
    return a


def LCM(a, b):
    return (a*b)//GCM(a, b)


for _ in range(int(input())):
    a, b = map(int, input().split())
    sol(a, b)
    print(LCM(a, b), GCM(a, b))

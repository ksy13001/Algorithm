import sys
"""
4
11 3 0 0
11 3 20 20
11 3 6 1
100000000 2 0 0
"""


def sol():
    n, k, vo, vk = map(int, input().split())
    # k 로 딱 떨어지고 vk가 충분한 경우
    if n - k * vk == 0:
        print(0)
    # vk 가 충분하지 않은 경우 일단 빼기
    elif n - k * vk > 0:
        n -= k * vk
        # vo 가 충분하다면
        if n <= vo:
            print(0)
            return
        else:
            a = (n - vo) // k + (n - vo) % k
            b = ((n - vo) // k) + 1
            if b * k - (n - vo) <= vo:
                print(min(a, b))
            else:
                print(a)
            return
    # k 로 딱 떨어지지 않고 vk 가 충분한 경우
    else:
        n %= k
        if n <= vo:
            print(0)
            return
        else:
            a = (n - vo) // k + (n - vo) % k
            b = ((n-vo)//k)+1
            if b*k - (n-vo) <= vo:
                print(min(a,  b))
            else:
                print(a)
            return
    return


for _ in range(int(input())):
    sol()

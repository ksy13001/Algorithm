from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
num = list(map(int, input().split()))
num.sort()


def get_range(k):
    l = bisect_left(num, k)
    r = bisect_right(num, k)
    if l == r:
        return -1
    return r - l


print(get_range(x))

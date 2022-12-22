import math
n, m = map(int, input().split())


def search(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True


for i in range(n, m+1):
    if search(i):
        print(i)

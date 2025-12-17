import sys
input = sys.stdin.readline

n = int(input())
s = 0
ans = []

for i in range(n):
    data = input().split()
    query = data[0]
    if query == "all":
        s = (1<<20) -1
    elif query == "empty":
        s = 0
    else:
        bit = 1 << int(data[1]) - 1
        if query == "add":
            s |= bit
        elif query == "remove":
            s &= ~bit
        elif query == "check":
            if s & bit:
                print(1)
            else:
                print(0)
        elif query == "toggle":
            s ^= bit

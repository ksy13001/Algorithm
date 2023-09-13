import sys
input = sys.stdin.readline


def sol():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for i in range(m)]
    arr.sort(key=lambda x: (x[1], x[0]))
    visited = []
    for li in arr:
        for i in range(li[0], li[-1]+1):
            if i not in visited:
                visited.append(i)
                break
            if len(visited) == n:
                print(n)
                return
    print(len(visited))
    return


for _ in range(int(input())):
    sol()

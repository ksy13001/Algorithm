import sys
input = sys.stdin.readline

def reverse(x, y, arr1):
    for i in range(3):
        for j in range(3):
            if arr1[x+i][y+j] == 0 : arr1[x+i][y+j] = 1
            else: arr1[x+i][y+j] = 0


def check(x, y, arr1, arr2):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if arr1[i][j] != arr2[i[j]]:
                cnt += 1
    return cnt

def sol():
    n, m = map(int, input().split())
    arr1 = []
    arr2 = []
    for _ in range(n):
        arr1.append(list(map(int, input().rstrip())))
    for _ in range(n):
        arr2.append(list(map(int, input().rstrip())))
    ans = 0
    for i in range(n-2):
        for j in range(m-2):
            if arr1[i][j] != arr2[i][j]:
                ans += 1
                reverse(i, j, arr1)
    for i in range(n):
        for j in range(m):
            if arr1[i][j] != arr2[i][j]:
                print(-1)
                return
    print(ans)
sol()

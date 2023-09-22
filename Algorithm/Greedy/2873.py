import sys
input = sys.stdin.readline


def sol():
    n, m = map(int, input().split())
    arr = []
    for i in range(n): arr.append(list(map(int, input().split())))
    # 세로 홀수
    if m % 2 == 1:
        for i in range(m):
            if i % 2 == 0:
                print('D'*(n-1), end='')
            else:
                print('U'*(n-1), end='')
            if i != m-1:
                print('R', end='')
    # 가로 홀수
    elif n % 2 == 1:
        for i in range(n):
            if i % 2 == 0:
                print('R'*(m-1), end='')
            else:
                print('L'*(m-1), end='')
            if i != n-1:
                print('D', end='')

    # N, M 짝수, 모두 더하기 불가능, 최소값 하나 제외
    elif n % 2 == 0 and m % 2 == 0:
        k = 1000
        s = 0
        x = 0
        y = 0
        # 최소값 찾기
        for i in range(n):
            for j in range(m):
                if (i % 2 == 1 and j % 2 == 0) or (i % 2 == 0 and j % 2 == 1):
                    if k > arr[i][j]:
                        k, tx, ty, = arr[i][j], i, j
        visited = False
        nx, ny = 0, 0
        ans = ''
        on = False
        while nx < n and ny < m:
            # RDLR
            if ty == 0 and ny == 0:
                for i in range(1, n, 2):
                    if i == tx:
                        # 끝
                        if i == n-1:
                            ans += 'RD'
                        else:
                            ans += 'RDDLD'
                    else:
                        # 끝
                        if i == n-1:
                            ans += 'R'
                        else:
                            ans += 'RDLD'
                ny += 1
                on = True
            elif ny + 1 == ty:
                # ty 짝수 -> up
                if ty % 2 == 1:
                    for i in range(0, n-1, 2):
                        if i == tx:
                            ans += 'D'
                        else:
                            ans += 'RDLD'
                    ans += 'R'
                # ty 홀수 -> down
                else:
                    for i in range(n-1, 0, -2):
                        if i == tx:
                            ans += 'U'
                        else:
                            ans += 'RULU'
                    ans += 'R'
                ny += 1
                on = True
            else:
                if not on:
                    if ny % 2 == 1:
                        ans += 'U'*(n-1)
                    else:
                        ans += 'D'*(n-1)
                else:
                    if ny % 2 == 0:
                        ans += 'U'*(n-1)
                    else:
                        ans += 'D'*(n-1)
            if ny != m-1:
                ans += 'R'
            ny += 1
        print(ans)
        return

"""
4 4
1 2 3 4
2 3 4 5
3 1 5 6
4 5 6 7
RDLDDRRDDDRUUU
"""
sol()

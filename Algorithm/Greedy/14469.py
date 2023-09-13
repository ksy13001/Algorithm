import sys
input = sys.stdin.readline


def sol():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    # 현재 시간
    time = 0
    for i in range(n):
        if time == 0:
            time += arr[i][0] + arr[i][1]
        else:
            # 현재 시간이 도착 시간 보다 많으면 바로 검문
            if time > arr[i][0]:
                time += arr[i][1]
            # 아니면 도착 시간 까지 대기
            else:
                time = arr[i][0] + arr[i][1]

    print(time)

sol()

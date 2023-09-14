import sys, math
input = sys.stdin.readline


def sol():
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr.sort()
    end = arr[0][0]
    cnt = 0
    for i in range(n):
        # 직전 작업 지점이 다음 작업 지점과 겹치지 않을 경우 end = arr[i][0]
        if end < arr[i][0] or end == arr[0][0]:
            end = arr[i][0]
        else:
            arr[i][0] = end + 1
            end = arr[i][0]
        #print('start:', end)
        temp = math.ceil((arr[i][1] - arr[i][0]) / k)
        end += k * temp - 1
        cnt += temp
        #print('end:',end)
    print(cnt)

sol()


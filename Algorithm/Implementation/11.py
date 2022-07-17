from collections import deque
n = int(input())
k = int(input())
stage = [[0 for _ in range(n)]for _ in range(n)]
dir = []
cur_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
time = 0
result = 0
i = 0
snake_size = 0
route = []
snake = deque()
snake.append((0, 0))
for _ in range(k):
    a, b = map(int, input().split())
    stage[b-1][a-1] = 1
#뱀의 방향 변환 정보
l = int(input())
for _ in range(l):
    a, b = map(str, input().split())
    dir.append((int(a), b))
cnt = 0
while True:
    print('*'*40)
    cur = snake.pop()
    route.append(cur)
    print("현재위치 : ", cur)
    print('time: ', time)
    print('snake size : ', len(snake)+1)
    print("route : ", route)
    if cur[0] >= n or cur[1] >= n or cur[0] < 0 or cur[1] < 0:
        print("범위를 벗어남")
        break
    if cur in snake:
        print("겹침")
        break
    if stage[cur[0]][cur[1]] == 1:
        print("사과발견 지점 : ", cur)
        snake_size += 1
        stage[cur[0]][cur[1]] = 0
    if time == dir[cnt][0]:
        if dir[cnt][1] == 'D':
            print("우회전***************")
            i += 1
        else:
            print("좌회전***************")
            i -= 1
        cnt += 1
        if cnt > 3:
            cnt = 0
    for k in range(snake_size):
        snake.append(route[len(route)-1-k])
    snake.append((cur[0] + cur_dir[i][0], cur[1] + cur_dir[i][1]))
    print('snake : ',*snake)
    time += 1

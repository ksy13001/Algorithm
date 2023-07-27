from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]


def bfs(sx, sy):
    q = deque([])
    # 키 비트마스킹으로 표현
    key = 0
    # 이동 횟수
    cnt = 0
    q.append((sx, sy, key, cnt))
    # 방문 기록을 이중리스트로 정하면 key를 얻은 루트와 key가 없는 루트가 겹침 -> key를 얻지 못했는데도 문 따고 들어가버림
    # 그렇다고 visited 리스트 없애면 무한반복
    # 방문기록을 현재 키값에 따른 (x, y) / 3중 리스트로 만든다 -> visited[x][y][key] / 1<<6 : 열쇠개수 6개(1000000)
    visited = [[[False for _ in range(1<<6)]for _ in range(m)]for _ in range(n)]
    while q:
        x, y, key, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny][key]:
                if 97 <= ord(graph[nx][ny]) <= 122: # a ~ z, 키 획득
                    k = ord(graph[nx][ny]) - 97
                    """
                    key|(1<<ord(graph[nx][ny]) - 97)
                    ->  if key == 'a':
                            ord('a')-97 = 0 이므로 1<<0 -> 1(0b000001)
                        if key == 'c':
                            ord('c')-97 = 2 이므로 1<<2 -> 4(0b000101)
                    획득한 키 추가 -> key|(1<<ord(graph[nx][ny]))
                    ex) a 키를 가진 상황에서 c 키 획득
                        -> key = key | (1<<2)) / 0b000001 | 0b0001                    
                    비트마스킹에서
                    & -> 어떤 이진수에서 값이 1인지 확인할 때 사용
                    | -> 어떤 이진수에 1을 추가하려 할 때 사용
                    """
                    visited[nx][ny][key|(1<<k)] = True
                    q.append((nx, ny, key|(1<<k), cnt+1))
                elif 65 <= ord(graph[nx][ny]) <= 90: # A ~ Z
                    k = ord(graph[nx][ny])-65
                    # 현재 k 값이 key 값에 있는지 확인, 값이 0이 아니면 참
                    if key & (1<<k):
                        visited[nx][ny][key] = True
                        q.append((nx, ny, key, cnt+1))
                elif graph[nx][ny] == '.' or graph[nx][ny] == '0':
                    visited[nx][ny][key] = True
                    q.append((nx, ny, key, cnt+1))
                elif graph[nx][ny] == '1':
                    visited[nx][ny][key] = True
                    return cnt+1
    return -1



for i in range(n):
    for j in range(m):
        if graph[i][j] == '0':
            print(bfs(i, j))
            break

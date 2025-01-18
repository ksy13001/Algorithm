from collections import deque
#https://atcoder.jp/contests/abc389/tasks/abc389_c
que = deque([])

n = int(input())
two_cnt = 0
pop = [0]
for _ in range(n):
    query = input()
    # print("query = ", query)
    if query[0] == '1':
        q, l = map(int, query.split(' '))
        if not que:
            que.append([l, 0, two_cnt])
        else:
            que.append([l, que[-1][0] + que[-1][1] - (pop[-1]-pop[que[-1][2]]), two_cnt])

    elif query[0] == '2':
        now = que.popleft()
        two_cnt += 1
        pop.append(pop[-1] + now[0])
    else:
        q, index = map(int, query.split(' '))
        print(que[index-1][1] - (pop[-1]-pop[que[index-1][2]]))
    # print("que:",que)
    # print("pop:",pop)
    # print()

# 10 15 0
# 20 10 15 0
# 45 25 15 0

# 0 15 10 20
# 0 15 25 45

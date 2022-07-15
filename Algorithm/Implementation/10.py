def rotate(key):
    rot = [[0 for _ in range(len(key))]for _ in range(len(key))]
    for i in range(len(key)):
        for j in range(len(key)):
            rot[i][len(key)-1-j] = key[j][i]
    return rot


def go_right(key):
    for i in range(len(key)):
        key[i].pop()
        key[i].insert(0, 0)
        print(key)


def go_down(key):
    key.append([0]*len(key))
    key.pop(0)


def solution(key, lock):
    target = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                target.append((i, j))


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

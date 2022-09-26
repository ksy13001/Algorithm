import sys
input = sys.stdin.readline
n, tape_len = map(int, input().split())
holes = list(map(int, input().split()))
tape_cnt = 0
holes.sort()
now = 0
now_hole = holes[0] - 0.5
next_hole = now_hole + tape_len

while True:
    for i in range(len(holes)):
        if now_hole < holes[i] < next_hole:
            now = i + 1
    tape_cnt += 1
    if now >= n:
        break
    now_hole = holes[now] - 0.5
    next_hole = now_hole + tape_len
print(tape_cnt)

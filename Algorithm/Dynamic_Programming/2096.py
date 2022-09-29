import sys
import copy
input = sys.stdin.readline
n = int(input())
graph = []
a, b, c = map(int, input().split())
dp_max = [a, b, c]
dp_min = [a, b, c]

dp_temp_max = [a, b, c]
dp_temp_min = [a, b, c]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    for i in range(3):
        if i == 0:
            dp_max[i] = a + max(dp_temp_max[0], dp_temp_max[1])
            dp_min[i] = a + min(dp_temp_min[0], dp_temp_min[1])
        elif i == 1:
            dp_max[i] = b + max(dp_temp_max[0], dp_temp_max[1], dp_temp_max[2])
            dp_min[i] = b + min(dp_temp_min[0], dp_temp_min[1], dp_temp_min[2])
        else:
            dp_max[i] = c + max(dp_temp_max[2], dp_temp_max[1])
            dp_min[i] = c + min(dp_temp_min[2], dp_temp_min[1])
    dp_temp_max = copy.deepcopy(dp_max)
    dp_temp_min = copy.deepcopy(dp_min)

print(max(dp_max), min(dp_min))

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
pack = 1000
line = 1000
result = 0
for _ in range(m):
    a, b = map(int, input().split())
    pack = min(a, pack)
    line = min(b, line)

if pack*(n //6) < n * line:
    result += pack*(n //6)
    n %= 6
else:
    result += n * line
    n = 0

if 0 < n < 6:
    if pack < n * line:
        result += pack
    else:
        result += n * line

print(result)

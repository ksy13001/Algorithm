n = int(input())
m = list(map(int, input().split()))+[0, 0] # 3, 5, 7
result = 0
for i in range(n):
    target = min(m[i:i + 3])
    if target > 0:
        if m[i+1] > m[i+2]:
            target = min(m[i+1] - m[i+2], m[i])
            for j in range(2): m[i + j] -= target
            result += 5 * target
        if m[i] > 0:
            target = min(m[i:i + 3])
            for j in range(3): m[i + j] -= target
            result += 7 * target
    else:
        target = min(m[i:i+2])
        if target > 0:
            for j in range(2): m[i + j] -= target
            result += 5 * target
    if m[i] > 0:
        result += 3 * m[i]
        m[i] = 0
print(result)

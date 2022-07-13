n = int(input())
m = list(map(int, input().split())) # 3, 5, 7
result = 0
for _ in range(2): m.append(0)
for i in range(n):
    while m[i] > 0:
        if m[i + 1] > 0:
            if m[i + 2] > 0:
                result += 7
                for j in range(3):
                    m[i+j] -= 1
            else:
                result += 5
                for j in range(2):
                    m[i+j] -= 1
        else:
            result += 3
            m[i] -= 1
print(result)

s = list(map(int, input()))
result = 0

for i in s:
    if i == 0 or i == 1:
        result += i
    elif result <= 1:
        result += i
    else:
        result *= i

print(result)

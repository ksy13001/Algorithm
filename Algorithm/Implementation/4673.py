num = []
for i in range(1, 10001):
    temp = sum(map(int, str(i))) + i
    num.append(temp)
num = list(set(range(1, 10000)) - set(num))
num.sort()
for i in range(len(num)):
    print(num[i])

import re
n = input()
result = 0
ch = []
for i in n:
    if i.isdigit():
        result += int(i)
    else:
        ch.append(ord(i))
ch.sort()
ch = list(map(chr, ch))+[result]
for i in ch:
    print(i, end='')

from collections import Counter
room = list(map(int, input()))
count = dict(Counter(room))
if 6 not in count:
    count[6] = 0
if 9 not in count:
    count[9] = 0

if 6 in count or 9 in count:
    if count[6] < count[9]:
        while count[6] < count[9]:
            count[9] -= 1
            count[6] += 1
    if count[6] > count[9]:
        while count[6] > count[9]:
            count[6] -= 1
            count[9] += 1

result = max(count.values())
print(result)

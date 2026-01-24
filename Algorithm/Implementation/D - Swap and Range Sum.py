n, q = map(int, input().split())

arr = list(map(int, input().split()))
sums = [0]
for a in arr:
    sums.append(sums[-1] + a)

for _ in range(q):
    query = input()
    if query[0] == "1":
        query = list(query.split())
        idx = int(query[1])
        sums[idx] = sums[idx-1] + sums[idx+1] - sums[idx]
    elif query[0] == "2":
        query = list(query.split())
        start, end = int(query[1]), int(query[2])
        print(sums[end]-sums[start-1])

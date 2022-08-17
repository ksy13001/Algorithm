import heapq

n = int(input())
q = []
result = 0
for _ in range(n):
    p = int(input())
    heapq.heappush(q, p)

while len(q) > 1:
    x = heapq.heappop(q)
    y = heapq.heappop(q)
    result += x + y
    heapq.heappush(q, x+y)
print(result)

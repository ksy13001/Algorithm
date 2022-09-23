import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
dia = []
bag = []
dia_value = []
result = 0
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(dia, (a, b))
for _ in range(k):
    heapq.heappush(bag, int(input()))
for i in range(len(bag)):
    bag_weight = heapq.heappop(bag)
    while dia and dia[0][0] <= bag_weight:
        weight, value = heapq.heappop(dia)
        if weight <= bag_weight:
            heapq.heappush(dia_value, -value)
    if dia_value:
        result -= heapq.heappop(dia_value)
print(result)

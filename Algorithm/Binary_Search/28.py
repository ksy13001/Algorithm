n = int(input())
num = list(map(int, input().split()))
start = 0
end = len(num) - 1
result = -1
while start <= end:
    mid = (start + end)//2
    if num[mid] == mid:
        result = mid
        break
    if mid > num[mid]:
        start = mid + 1
    else:
        end = mid - 1

print(result)

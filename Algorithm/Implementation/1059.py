n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l = int(input())
start = 0
end = 0
if l in arr:
    print(0)
else:
    if l < arr[0]:
        arr = [0] + arr
    for i in range(1, n):
        if l in range(arr[i-1]+1, arr[i]):
            start = arr[i-1] + 1
            end = arr[i] - 1
            break
    print((l - start) * (end - l + 1) + (end - l))

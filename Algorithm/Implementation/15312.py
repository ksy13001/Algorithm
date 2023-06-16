cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
a = list(map(lambda x: cnt[ord(x)-65], list(input())))
b = list(map(lambda x: cnt[ord(x)-65], list(input())))
arr = sum([[a[i], b[i]] for i in range(len(a))], [])
while len(arr) != 2:
    arr = [(arr[i]+arr[i+1])%10 for i in range(len(arr)-1)]
print("".join(map(str, arr)))

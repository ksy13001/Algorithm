def sol():
    arr = list(map(int, input().split()))
    n = arr[0]
    dic = {}
    for i in range(1, n+1):
        if arr[i] not in dic:
            dic[arr[i]] = 1
        else:
            dic[arr[i]] += 1
    arr = list(sorted(dic.items(), key=lambda x:-x[1]))
    if arr[0][1] > n//2:
        print(arr[0][0])
    else:
        print("SYJKGW")
for _ in range(int(input())):
    sol()

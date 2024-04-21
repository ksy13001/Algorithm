def sol():
    n = int(input())
    arr = list(map(int, input().split()))
    idx = [0 for _ in range(n+1)]   # arr에서 각 값이 담겨 있는 인덱스 위치
    ans = []
    for i in range(n):
        idx[arr[i]] = i+1

    for i in range(n):
        if arr[i] != i+1:   # arr[i] = 3, arr[idx[i+1]-1] = 3, idx[i+1] = 3
            k = arr[i]
            p = idx[i+1]
            ans.append((i+1, idx[i+1]))
            arr[i], arr[idx[i+1]-1] = arr[idx[i+1]-1], arr[i]
            idx[i+1], idx[k] = i+1, p
    print(len(ans))
    for a, b in ans:
        print(a, b)
    return
sol()

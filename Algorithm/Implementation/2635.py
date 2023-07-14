def sol():
    n = int(input())
    ans = 0
    ans_arr = []
    for i in range(1, n+1):
        arr = [n, i]
        cnt = 2
        while arr[-1] >= 0:
            arr.append(arr[cnt-2]-arr[cnt-1])
            cnt += 1
        if ans < cnt:
            ans = cnt
            ans_arr = arr
    return print(ans-1), print(*ans_arr)


sol()

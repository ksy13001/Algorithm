def solution():
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    min_arr = sorted((arr[i], i+1) for i in range(n))

    for _ in range(q):
        k = int(input())
        b = list(map(int, input().split()))

        for num, idx in min_arr:
            if idx not in b:
                print(num)
                break




solution()

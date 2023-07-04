def sol():
    n = int(input())
    for i in range(1, n+1):
        if i + sum(map(int, str(i))) == n:
            print(i)
            return
    print(0)
sol()

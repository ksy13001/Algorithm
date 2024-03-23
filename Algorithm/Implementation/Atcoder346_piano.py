def sol():
    w, b = map(int, input().split())
    s = 'wbwbwwbwbwbw'*20
    for i in range(12):
        arr = s[i:i+w+b]
        if arr.count('w') == w and arr.count('b') == b:
            print('Yes')
            return
    print('No')


sol()

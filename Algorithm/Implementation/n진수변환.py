def _10_to_n():
    n, b = map(int, input().split())
    ans = ''
    while n >= b:
        k = n % b
        if k >= 10:
            k = chr(k+55)
        ans += str(k)
        n //= b
    if n >= 10:
        ans += chr(n+55)
    else:
        ans += str(n)
    print(''.join(reversed(ans)))


def _n_to_10():
    n, b = map(str, input().split())
    n = list(map(lambda x: ord(x) - 55 if ord(x) >= 65 else int(x), n))
    ans = 0
    k = int(b)
    l = len(n)
    for i, v in enumerate(n):
        ans += (k ** (l - i - 1)) * v
    print(ans)

def fac(n):
    fact = 2
    factors = []
    while fact**2 <= n:
        while n%fact == 0:
            factors.append(fact)
            n //= fact
        fact += 1
    if n > 1:
        factors.append(n)
    return max(factors)


n = int(input())
k = int(input())
ans = 0
while n > 1:
    a = fac(n)
    if a <= k:
        ans += 1
    n -= 1
print(ans+1)

n = int(input())
coins = sorted(list(map(int, input().split())))
target = 1
for coin in coins:
    print(coin, ' : ',target)
    if target < coin:
        break
    target += coin
print(target)

n, m = map(int, input().split())
num = list(map(int, input().split()))
card = []
result = 0


def search(cnt):
    global result
    if cnt == 3:
        if sum(card) <= m:
            result = max(result, sum(card))
        return
    for i in range(len(num)):
        if num[i] not in card:
            card.append(num[i])
            search(cnt + 1)
            card.pop()


search(0)
print(result)

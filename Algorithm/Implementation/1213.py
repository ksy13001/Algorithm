def sol():
    st = list(input())
    dic = {}
    cnt = 0
    ans = ['0' for _ in range(len(st))]
    now = 0
    for i in set(st):
        dic[i] = st.count(i)
        if dic[i] % 2 == 1:
            cnt += 1
    if cnt > 1:
        print("I'm Sorry Hansoo")
        return 0

    for s, c in sorted(dic.items()):
        if c % 2 == 1:
            ans[len(st)//2] = s
        for _ in range(c//2):
            ans[now] = s
            now += 1
    k = len(st)//2 + 1
    if len(st) % 2 == 1:
        print(''.join(ans[:k] + list(reversed(ans[:k-1]))))
    else:
        print(''.join(ans[:k-1] + list(reversed(ans[:k - 1]))))
    return
sol()

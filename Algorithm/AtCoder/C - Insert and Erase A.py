def solution():
    s = input()
    t = input()

    if s.replace("A", "") != t.replace("A", ""):
        print(-1)
        return
    s_idx, t_idx, ans = 0, 0, 0

    while s_idx < len(s) or t_idx < len(t):
        s_cnt, t_cnt = 0, 0

        while s_idx < len(s) and s[s_idx] == "A":
            s_idx += 1
            s_cnt += 1

        while t_idx < len(t) and t[t_idx] == "A":
            t_idx += 1
            t_cnt += 1

        if s_idx < len(s) and t_idx < len(t):
            s_idx += 1
            t_idx += 1

        ans += abs(s_cnt - t_cnt)

    print(ans)


solution()

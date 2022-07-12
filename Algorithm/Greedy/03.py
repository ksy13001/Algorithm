s = input()
cnt1 = 0
cnt0 = 0
for i in range(len(s)):
    cur = s[i]
    if s[i-1] != cur: 
        if s[i - 1] == '1':
            cnt1 += 1
        else:
            cnt0 += 1
print(min(cnt0, cnt1))

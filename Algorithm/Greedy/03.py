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
"""
s = input()
now = s[-1]
one = 0
zero = 0
for st in s:
    if st == '0':
        if now == '1':
            now = '0'
            zero += 1
    if st == '1':
        if now == '0':
            now = '1'
            one += 1

print(min(one, zero))
"""

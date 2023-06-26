
#replace 이용하여 아주 쉽게 풀이 가능
s = input()
s1 = s.replace('XXXX', 'AAAA')
s2 = s1.replace('XX', 'BB')
if 'X' in s2:
    print(-1)
else:
    print(s2)


def sol():
    s = input().split('.')
    arr = []
    for i in range(len(s)):
        if s[i] == '':
            arr.append('.')
        else:
            n = len(s[i])
            if n % 2 == 0:
                if n >= 4:
                    arr.append('AAAA'*(n//4)+'B'*(n%4))
                elif n >= 2:
                    arr.append('BB')
                arr.append('.')
            else:
                print(-1)
                return 0
    print(''.join(arr[:-1]))

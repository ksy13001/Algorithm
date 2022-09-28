'''
  나머지 분배 법칙
  (AxB)%C = (A%C) *(B%C) % C
'''

a, b, c = map(int, input().split())
result = 0


def calculate(a, b):
    if b == 1:
        return a % c
    else:
        temp = calculate(a, b//2)
        if b % 2 == 0:
            return (temp * temp)%c
        else:
            return (temp * temp * a) % c


print(calculate(a, b))

n = 3
print('짝수' if n % 2 == 0 else '홀수')

a = [1, 2, 3, 4, 5, 6, 7]

b = [i for i in a if i % 2 == 0]
print(b)


b = [i if i % 2 == 0 else 0 for i in a]
print(b)

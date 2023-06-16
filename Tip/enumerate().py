# enumerate -> (인덱스,원소) 튜플 반환
a = [1, 3, 5]

for i in enumerate(a):
    print(i)
    """
    (0, 1)
    (1, 3)
    (2, 5)
    """

for i, now in enumerate(a):
    print(i, now)
    """
    0 1
    1 3
    2 5
    """

for i in enumerate(a, start=1): # 인덱스가 1부터 시작
    print(i)

# 2차원 리스트 루프

matrix = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
for r, row in enumerate(matrix):
    for k, letter in enumerate(row):
        print(r, k , letter)

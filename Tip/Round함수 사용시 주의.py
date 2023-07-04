# round 함수는 짝수로 반올림
print(round(2.5)) # 2
print(round(1.5)) # 2


def round2(n):
  return int(n) + 1 if n - int(n) >= 0.5 else int(n)

print(round2(2.5)) # 3
print(round2(1.5)) # 2

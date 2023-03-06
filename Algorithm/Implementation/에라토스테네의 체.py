import math
"""
1. 2~n 까지 모든 자연수 나열
2. 나열된 수 중 가장 작은수 x 지정
3. 나열 된 수 중 x 배수 제거
4. 2,3 반복

"""

n = int(input())
arr = [True] * (n + 1) #n 까지 자연수 소수로 두기
arr[0], arr[1] = False, False # 0,1 은 소수 x
for i in range(2, int(math.sqrt(n))+1): # 2 ~ n 까지
  if arr[i]: # i가 소수면
    j = 2
    while i * j <= n:
      # i 제외 n 이하 i의 배수 모두 삭제
      arr[i * j] = False
      j += 1

ans = []
for i in range(2, n+1):
  if arr[i]:
    ans.append(i)
  

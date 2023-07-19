def sol():
    n = int(input())
    ans = [100] * n
    arr = list(map(int, input().split()))
    for num, now in enumerate(arr):
        # num = 현재 사람 키, now = 왼쪽에 자신보다 큰 사람 수
        cnt = 0
        # 정답 리스트 탐색
        for i in range(n):
            # 나보다 키큰사람 == now 면 빈자리 일때 ans 값 갱신
            if cnt == now and ans[i] == 100:
                ans[i] = num+1
                break
            # 키가 나보다 크면 cnt += 1
            if ans[i] > num+1:
                cnt += 1
    print(*ans)
    return


sol()


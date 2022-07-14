def solution(s):
    array = []
    result = []
    answer = len(s) + 1
    cnt = 1
    for length in range(1, len(s)+1):
        for i in range(0, len(s), length): array.append(s[i:i+length])
        array.append('0')
        for j in range(len(array)-1):
            if array[j] == array[j+1]:
                cnt += 1
            else:
                if cnt >1:
                    result.append(f"{cnt}{array[j]}")
                else:
                    result.append(f"{array[j]}")
                cnt = 1
        result = "".join(result)
        answer = min(len(result), answer)
        array = []
        result = []
    return answer

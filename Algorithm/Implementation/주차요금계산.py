import math
def solution(fees, records):
    answer = []
    dic = {}
    s = []
    time = []
    for i in range(len(records)):
        s.append(list(map(str, records[i].split())))
    for j in range(len(records)):
        st = list(map(int, s[j][0].split(':')))
        time.append((st[0], st[1]))
    for i in range(len(records)):
        name, mode = s[i][1], s[i][2]
        if name in dic:
            nt, now_value = dic[name]
        if mode == 'IN':
            if name not in dic:
                dic[name] = [[time[i][0], time[i][1]], 0]
            else:
                dic[name] = [[time[i][0], time[i][1]], now_value]
        else:
            dic[name] = [0, now_value+(time[i][0]-nt[0])*60 + (time[i][1]-nt[1])]
    for key, val in dict(sorted(dic.items())).items():
        if val[0] != 0:
            val[1] += (23-val[0][0]) * 60 + (59-val[0][1])
        if fees[0] >= val[1]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + (math.ceil((val[1] - fees[0]) / fees[2]) * fees[3]))
    return answer

"""
print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
                                "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
"""

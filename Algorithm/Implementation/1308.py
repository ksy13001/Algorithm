"""
2000 1 1
2401 1 1
"""

"""
def cal(n):
    global year, month, day
    if month in (1, 3, 5, 7, 8, 10, 12) and day == 32:
        month += 1
        day = 1
    elif month in (4, 6, 9, 11) and day == 31:
        month += 1
        day = 1
    elif month == 2: # month == 2:
        if n == 29: #윤년
            if day == 30:
                month += 1
                day = 1
        else:   #평년
            if day == 29:
                month += 1
                day = 1
    if month == 13:
        month = 1
        year += 1


year, month, day = map(int, input().split())
ty, tm, td = map(int, input().split())
cnt = 0
if (ty - year == 1000 and tm >= month and td >= day )or ty - year > 1000:
    print('gg')
else:
    while True:
        if year == ty and month == tm and day == td:
            print(f'D-{cnt}')
            break
        day += 1
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    cal(29) # 윤년
                else:
                    cal(30) # 평년
            else:
                cal(29) # 윤년
        else:
            cal(30)
        cnt += 1
"""
#datetime 사용
import datetime as dt
year, month, day = map(int, input().split())
ty, tm, td = map(int, input().split())
if (ty - year == 1000 and tm >= month and td >= day )or ty - year > 1000:
    print('gg')
else:
    print(f'D-{(dt.datetime(ty, tm, td) - dt.datetime(year, month, day)).days}')

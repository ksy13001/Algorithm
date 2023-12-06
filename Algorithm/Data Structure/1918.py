from collections import deque
s = input()
st = []
for now in s:
    # 괄호인 경우
    if now == '(':
        st.append(now)
    elif now == ')':
        while st:
            k = st.pop()
            if k == '(':
                break
            else:
                print(k, end='')
    # 기호인 경우
    elif now == '*' or now == '/':
        while st and (st[-1] == '*' or st[-1] == '/'):
            print(st.pop(), end='')
        st.append(now)
    elif now == '+' or now == '-':
        while st and st[-1] != '(':
            print(st.pop(), end='')
        # st 의 *, / 모두 출력
        st.append(now)
    # 문자인 경우 순서대로 바로 출력
    else:
        print(now, end='')
# 남은거 출력
while st:
    temp = st.pop()
    if temp != '(':
        print(temp, end='')

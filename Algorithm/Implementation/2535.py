n = int(input())
grade = []
for _ in range(n):
    a, b, c = map(int, input().split())
    grade.append((a, b, c))
country = [0 for _ in range(grade[-1][0] + 1)]

grade.sort(key=lambda x:-x[2])
ans = []
for c, num, val in grade:
    if country[c] < 2:
        country[c] += 1
        ans.append((c, num))
    if len(ans) == 3:
        break
for i in range(3):
    print(*ans[i])

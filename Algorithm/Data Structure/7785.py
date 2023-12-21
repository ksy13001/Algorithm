company = set()
for _ in range(int(input())):
    a, b = map(str, input().split())
    if b == 'enter':
        company.add(a)
    elif a in company:
        company.remove(a)
company = list(company)
company.sort(reverse=True)
for i in company:
    print(i)

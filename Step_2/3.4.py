from datetime import datetime, timedelta

data = ['Иван Петров 30.12.1997',
        'Петр Сергеев 04.01.1992',
        'Сергей Иванов 03.01.1996',
        'Маша Иванова 30.12.1994',
        'Григорий Иванов 03.12.1995']


m_str = '29.12.2021'


fmt = '%d.%m.%Y'
date = datetime.strptime(m_str, fmt)
emps = [(datetime.strptime(d, fmt), ' '.join(n)) \
        for *n, d in (i.split() for i in data)]
ucbd = [*filter(lambda x: 0 < (x[0].replace(year = date.year) - date).days <= 7, emps)]

print(max(ucbd)[1] if ucbd else 'Дни рождения не планируются')



# fmt = '%d.%m.%Y'
# date = datetime.strptime(input(), fmt)
# emps = [(datetime.strptime(d, fmt), ' '.join(n)) \
#         for *n, d in (input().split() for _ in range(int(input())))]
# ucbd = [*filter(lambda x: 0 < (x[0].replace(year = date.year) - date).days <= 7, emps)]
#
# print(max(ucbd)[1] if ucbd else 'Дни рождения не планируются')
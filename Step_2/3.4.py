from datetime import datetime, timedelta

data = ['Иван Петров 30.12.1997',
        'Петр Сергеев 04.01.1992',
        'Сергей Иванов 03.01.1996',
        'Маша Иванова 30.12.1994',
        'Григорий Иванов 03.12.1995']


m_str = '29.12.2021'
a_name = 'Дни рождения не планируются'
min_bd = datetime(day=31, month= 12, year=9999)
# a_data = datetime.strptime(input(), '%d.%m.%Y')
# a_data = datetime.strptime(m, '%d.%m.%Y')
dat_set = set(map(lambda k: (k.day, k.month), [datetime.strptime(m_str, '%d.%m.%Y') + timedelta(days=j) for j in range(1, 8)]))
print(dat_set)

# for i in sorted([input().split() for _ in range(int(input()))], key=lambda j: datetime.strptime(j[2], '%d.%m.%Y')):
for i in data:
    b_data = datetime.strptime(i.split()[2], '%d.%m.%Y')
    if (b_data.day, b_data.month) in dat_set and b_data < min_bd:
        min_bd = b_data
        a_name = f'{i.split()[0]} {i.split()[1]}'
print(a_name)


# a_dict = {}
# for i in sorted([input().split() for _ in range(int(input()))], key=lambda j: datetime.strptime(j[2], '%d.%m.%Y')):
#     a_dict[i[2]] = a_dict.get(i[2], 0) + 1
# [print(k) for k, v in a_dict.items() if v == max(a_dict.values())]
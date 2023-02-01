from datetime import date, time, datetime, timedelta

data = ['Иван Петров 01.05.1995',
        'Петр Сергеев 01.07.1995',
        'Сергей Иванов 01.01.1996']

# d = {f'{i[0]} {i[1]}': datetime.strptime(i[2], '%d.%m.%Y') for i in [input().split() for i in range(int(input()))]}
d = {f'{i.split()[0]} {i.split()[1]}': datetime.strptime(i.split()[2], '%d.%m.%Y') for i in data}
d = dict(sorted(d.items(), key=lambda i: i[1]))
d2 = dict(filter(lambda k: k[1] == list(d.values())[0], d.items()))
if len(d2) == 1: print(list(d.values())[0].strftime('%d.%m.%Y'), *d2)
else:
    print(list(d.values())[0].strftime('%d.%m.%Y'), len(d2))



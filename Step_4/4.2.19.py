import csv
from datetime import datetime


def write_csv_list(filename: str, lst: list, col: list, deli=','):
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=col, delimiter=deli)
        writer.writeheader()
        writer.writerows(lst)


if __name__ == '__main__':
    columns, row_dict = ['username', 'email', 'dtime'], dict()
    with open('name_log.csv', 'r', encoding='utf-8') as file:
        for st in csv.DictReader(file, delimiter=','):
            if st['email'] in row_dict:
                if datetime.strptime(st['dtime'], '%d/%m/%Y %H:%M') > datetime.strptime(row_dict[st['email']][1],
                                                                                        '%d/%m/%Y %H:%M'):
                    row_dict[st['email']] = (st['username'], st['dtime'])
            else:
                row_dict[st['email']] = (st['username'], st['dtime'])

    nw_list = list(map(lambda i: {'username': i[1][0], 'email': i[0], 'dtime': i[1][1]}, sorted(row_dict.items())))
    write_csv_list('new_name_log.csv', nw_list, columns)

    with open('name_log.csv', encoding='UTF-8') as f:
        header, *rows = csv.reader(f)

    d = {i[1]: i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}

    with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(sorted(d.values(), key=lambda x: x[1]))

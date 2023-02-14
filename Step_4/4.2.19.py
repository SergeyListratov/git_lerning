import csv


def read_csv_list(filename: str, deli=',') -> list:
    with open(filename, 'r', encoding='utf-8') as file:
        data_list = list(csv.DictReader(file, delimiter=deli))
        return data_list


def write_csv_list(filename: str, lst: list, col: list, deli=','):
    with open(filename, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=col, delimiter=deli)
        writer.writeheader()
        writer.writerows(lst)


def email_div(st: str) -> str:
    return st[(st.find('@') + 1):]


if __name__ == '__main__':
    columns, row_dict = ['domain', 'count'], dict()
    for st in read_csv_list('name_log.csv'):
        row_dict[email_div(st['email'])] = row_dict.get(email_div(st['email']), 0) + 1
    new_list = [{'domain': t[0], 'count': t[1]} for t in sorted(row_dict.items())]
    write_csv_list('domain_usage.csv', sorted(new_list, key=lambda i: i['count']), columns)

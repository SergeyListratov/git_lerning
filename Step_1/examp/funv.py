import random


def generate_pin(length: int) -> str:
    return ''.join(str(random.randint(0, 9)) for _ in range(length))


def replace_five_inplace(a_list: list, value: str):
    for index in range(len(a_list)):
        a_list[index] = a_list[index].replace('6', value)


if __name__ == '__main__':
    b_list = [generate_pin(6), generate_pin(5)]
    print(b_list)
    replace_five_inplace(b_list, '2')
    print(b_list)



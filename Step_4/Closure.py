def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


def average():
    values = []

    def inner(value: int) -> float:
        values.append(value)
        return sum(values) / len(values)

    return inner


def counter():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner


def pow_(base):
    def inner(value):
        return value ** base

    return inner


def pow_1(base):
    return lambda value: value ** base


if __name__ == '__main__':
    p = pow_1(3)
    # pow_2 = pow_(3)
    print(p(4))
    # print(pow_2(3)
    # pow_ = pow_()


    # boys = names()
    # # girls = names()
    # print(boys('Vasya'))
    # print(boys.__closure__[0].cell_contents)

    # print(boys('Petya'))
    # print(boys('Dimaa'))
    # print(girls('Olya'))
    # print(girls('Sverta'))
    # print(girls('Ira'))
    # avg = average()
    # print(avg(10))
    # # print(avg(20))
    # # print(avg(30))
    # count = counter()
    # print(count(1))
    # print(count(1))
    # print(count(-3))


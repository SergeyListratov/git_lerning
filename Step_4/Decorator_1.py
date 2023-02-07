def logger(func):
    def wrapper(a, b):
        print(f'{func.__name__} started')
        result = func(a, b)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(a, b):   #В этот момент summ = wrapper
    return a + b


def example(a):
    def inner(b):
        print(a + b)

    inner(3)


if __name__ == '__main__':
    # function = logger(summ)
    # print(function(2, 3))
    # logger(summ)(2, 3)
    # summ = logger(summ)
    print(summ(2, 3))
    print(summ)

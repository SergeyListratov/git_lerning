def typed(type_):
    def real_decorator(function):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f'Тип данных должен быть {type_}')
            return function(*args)

        return wrapper

    return real_decorator


@typed(int)
def calculate(a, b, c):
    # logic
    return a + b + c


@typed(str)
def convert(a, b):
    # logic
    return a + b


if __name__ == '__main__':
    #calculate   ==  typed_int(calculate)
    print(calculate(1, 2, 3))
    print(convert('a', '2'))

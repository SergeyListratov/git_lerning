from typing import List, Union, Optional, Any


def calc(a: Union[int, float], b: int) -> Any:
    return a + b


def to_int(a_list: str) -> List[int]:
    return [int(e) for e in a_list]


if __name__ == '__main__':
    print(calc(2, 1))

'''docstring goes here...'''

def add_nums(x: int, y: int) -> int:
    return x + y

z = add_nums('car', 'boat')
print(z)

def add_nums_only_ints(x, y): # we could also add type hints if we wanted to.
    if not isinstance(x, int):
        raise TypeError(f'x should be an int, got {type(x)}')
    if not isinstance(y, int):
        raise TypeError(f'y should be an int, got {type(y)}')
    return x + y


z = add_nums_only_ints(2,3)
print(z)

z = add_nums_only_ints('car', 'boat')


def add_nums(x: int, y: int) -> int:
    """Add two numbers and return their sum.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return x + y



from typing import Any
from functools import reduce


def is_a_palindrome(value: str) -> bool:
    """ Checks if a given value is a `palindrome` """
    return value == value[::-1]

def main() -> None:
    value_to_check = input('Enter value to know if it is a palindrome: ')
    if is_a_palindrome(value_to_check):
        print(F'{ value_to_check } is a palindrome')
    else:
        print(F'{ value_to_check } is not a palindrome')


if __name__ == '__main__':
    main()

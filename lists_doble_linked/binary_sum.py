from collections import deque
from itertools import zip_longest


def by_significant_digit(binary_number):
    return list(map(int, reversed(binary_number)))


def binary_sum(n, n2):
    """
    n and n2 are non negative binary numbers with arbitrary len.
    """
    n = by_significant_digit(n)
    n2 = by_significant_digit(n2)
    carry = 0
    result = deque()

    for digit, digit2 in zip_longest(n, n2, fillvalue=0):
        actual_sum = carry + digit + digit2
        carry = 0 if actual_sum < 2 else 1
        result.appendleft(str(actual_sum % 2))
    if carry == 1:
        result.appendleft('1')

    return ''.join(result)


print(binary_sum('111110', '1100'))  # 1001010

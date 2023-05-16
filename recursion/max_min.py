def max_min(lst):
    """
    Calculate the maximum and the minimum of a list.
    :param lst: list
    :return: tuple: (max, min)
    """

    length = len(lst)
    if length == 0:
        raise ValueError('Empty List')

    max_value = min_value = lst[-1]

    """
    t(n) = 1 + t(n-1)
    t(n) = 1 + 1 + t(n-2)
    t(n) = 1 + 1 + 1 + n*1 + t(-1)
    t(n) = 3 + n + 1
    t(n) = O(n)

    m(n) = 1 + m(n-1)
    m(n) = 1 + 1 + m(n-2)
    m(n) = 1 + 1 + n*1 + m(-1)
    m(n) = O(n)
    """

    def max_min_rec(current_index):
        nonlocal max_value, min_value
        if current_index < 0:
            return max_value, min_value

        current_value = lst[current_index]
        if current_value > max_value:
            max_value = current_value
        if current_value < min_value:
            min_value = current_value

        return max_min_rec(current_index - 1)

    return max_min_rec(length - 1)


print(max_min(list(range(100))))

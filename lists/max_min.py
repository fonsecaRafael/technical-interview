def max_min_ordered_crescent_list(lst):
    """
    Calculate the maximum and the minimum of a list.
    :param lst: list
    :return: tuple: (max, min)
    """

    if len(lst) == 0:
        raise ValueError('Empty List')
    return lst[-1], lst[0]  # O(1)


def max_min_unordered_list(lst):
    """
    Calculate the maximum and the minimum of a list.
    :param lst: list
    :return: tuple: (max, min)
    """
    if len(lst) == 0:
        raise ValueError('Empty List')

    max_value, min_value = lst[0]
    for value in lst:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value

    return max_value, min_value  # O(n)

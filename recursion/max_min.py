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

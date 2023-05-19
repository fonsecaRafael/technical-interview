def remove_duplicates(lst):
    """
      Remove duplicates from lst.
      Linear complexity for time and space.
    :param lst: a list
    :return: new list without duplicated elements
    """
    result = []
    repeated = set()
    for element in lst:  # Para cada elemento da lista, complexidade linear
        if element not in repeated:  # in de set, complexidade constante
            result.append(element)
            repeated.add(element)
    # Sem o repeated, esse algoritmo teria complexidade quadrática
    return result


print(remove_duplicates([1, 1, 2, 3, 4, 5, 5, 5, 6]))

def hanoi(n, origin='A', aux='B', goal='C'):
    """
    Recursive solution to Hanoi Tower

    t(n)   = k + 2t(n-1)

    t(n) = k + 2t(n-1)
    t(n) = k + 2k + 4t(n-2)
    t(n) = k + 2k + 4k + 8t(n-3)
    t(n) = k + 2^n
    t(n) = 2^n

    m(n) = 1 + m(n-1) -1 + 1
    m(n) = O(n)
    """
    if n >= 1:
        hanoi(n-1, origin, goal, aux)  # t(n-1)
        print(f'{origin} -> {goal} : {n}')  # 1
        hanoi(n-1, aux, origin, goal)  # t(n-1)


for i in range(1, 4):
    print(f'############# Hanoi {i}')
    hanoi(i)

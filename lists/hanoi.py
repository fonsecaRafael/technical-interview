def hanoi(n, origin='A', aux='B', goal='C'):
    stack = [(False, n, origin, aux, goal)]

    while stack:
        print_flag, n, origin, aux, goal = stack.pop()
        if n < 1:
            continue

        if not print_flag:
            stack.append((True, n, origin, aux, goal))
            stack.append((False, n-1, origin, goal, aux))
        else:
            print(f'{origin} -> {goal} : {n}')
            stack.append((False, n-1, aux, origin, goal))


for i in range(1, 4):
    print(f'############# Hanoi {i}')
    hanoi(i)

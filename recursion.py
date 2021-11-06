def inf_recursion(number):
    a = number / 5
    if number != 0:
        inf_recursion(number)
    return 0


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_dynamic(n, memory={0: 1, 1: 1}):
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial_dynamic(n - 1)
        print(memory)
        return memory[n]

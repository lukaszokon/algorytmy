import timeit
from random import randint


def prepare_data(n):
    numbers_list = []
    for i in range(n):
        numbers_list.append(randint(1, n))
    numbers_list.sort()
    return numbers_list


def linear_search(element, numbers_list):
    for number in numbers_list:
        if number == element:
            return True
    return False


def binary_search(element, numbers_list):
    while len(numbers_list) > 0:
        mid = (len(numbers_list)) // 2
        if numbers_list[mid] == element:
            return True
        elif numbers_list[mid] < element:
            numbers_list = numbers_list[:mid]
        else:
            numbers_list = numbers_list[mid + 1:]
    return False


def linear_time(n):
    SETUP_CODE = '''
from __main__ import linear_search, prepare_data
from random import randint'''

    TEST_CODE = f'''
n = {n}
number_list = prepare_data(n)
linear_search(randint(1, n), number_list)'''
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100)
    print(f'Linear search time: {sum(times)/len(times)}')


def binary_time(n):
    SETUP_CODE = '''
from __main__ import binary_search, prepare_data
from random import randint'''

    TEST_CODE = f'''
n = {n}
number_list = prepare_data(n)
binary_search(randint(1, n), number_list)'''
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=3,
                          number=100)
    print(f'Binary search time: {sum(times)/len(times)}')


if __name__ == '__main__':
    times = [1, 10, 100, 1000]
    for time in times:
        print(f"Wyszukiwanie dla {time} elementów:")
        linear_time(time)
        binary_time(time)
        print()

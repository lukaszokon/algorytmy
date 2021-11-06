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


def linear_time():
    SETUP_CODE = '''
from __main__ import linear_search, prepare_data
from random import randint'''

    TEST_CODE = '''
n = 4000
number_list = prepare_data(n)
linear_search(randint(1, n), number_list)'''
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt= TEST_CODE,
                          repeat=3,
                          number=100)
    print(f'Linear search time: {min(times)}')


if __name__ == '__main__':
    linear_time()

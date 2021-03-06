from random import randint
import timeit


def prepare_data(n):
    random_list = []
    for i in range(n):
        random_list.append(randint(1, n))
    sorted_list = sorted(random_list)
    sorted_reversed_list = sorted_list[::-1]
    sorted_with_one_change = sorted_list.copy()

    # mid_index = n//2
    # temp_number = sorted_with_one_change[mid_index]
    # sorted_with_one_change[mid_index] = sorted_with_one_change[mid_index- 1]
    # sorted_with_one_change[mid_index - 1] = temp_number

    sorted_with_one_change[n // 2], sorted_with_one_change[n // 2 - 1] = sorted_with_one_change[n // 2 - 1], \
                                                                         sorted_with_one_change[n // 2]

    return random_list, sorted_list, sorted_reversed_list, sorted_with_one_change


def bubble_sort(list_to_sort):
    n = len(list_to_sort)
    for sorting_round in range(n):
        for index in range(n - 1):
            if list_to_sort[index] > list_to_sort[index + 1]:
                list_to_sort[index], list_to_sort[index + 1] = list_to_sort[index + 1], list_to_sort[index]


def bubble_sort_1(list_to_sort):
    n = len(list_to_sort) - 1
    m = n
    for sorting_round in range(n):
        for index in range(m):
            if list_to_sort[index] > list_to_sort[index + 1]:
                list_to_sort[index], list_to_sort[index + 1] = list_to_sort[index + 1], list_to_sort[index]
        m -= 1


def bubble_sort_2(list_to_sort):
    n = len(list_to_sort) - 1
    m = n
    for sorting_round in range(n):
        was_change = False
        for index in range(m):
            if list_to_sort[index] > list_to_sort[index + 1]:
                list_to_sort[index], list_to_sort[index + 1] = list_to_sort[index + 1], list_to_sort[index]
                was_change = True
        if not was_change:
            return
        m -= 1


def bubble_sort_3(list_to_sort):
    n = len(list_to_sort) - 1
    m = n
    start_index = 0
    for sorting_round in range(n):
        was_change = False
        for index in range(start_index, m):
            if list_to_sort[index] > list_to_sort[index + 1]:
                list_to_sort[index], list_to_sort[index + 1] = list_to_sort[index + 1], list_to_sort[index]
                if not was_change:
                    if index > 0:
                        start_index = index - 1
                    was_change = True
        if not was_change:
            return
        m -= 1


def insert_sort(list_to_sort):
    n = len(list_to_sort)
    for i in range(1, n):
        index = i
        while list_to_sort[index - 1] > list_to_sort[index]:
            list_to_sort[index - 1], list_to_sort[index] = list_to_sort[index], list_to_sort[index - 1]
            if index > 1:
                index -= 1
            else:
                break


def merge_sort(list_to_sort):
    # TODO
    pass


def quick_sort_init(list_to_sort):
    end_index = len(list_to_sort) - 1
    quick_sort(list_to_sort, 0, end_index)


def quick_sort(list_to_sort, start_index, end_index):
    # Wybieranie pivota
    middle = (start_index + end_index) // 2
    pivot = list_to_sort[middle]

    # Przerzucenie pivota na koniec listy
    list_to_sort[middle], list_to_sort[end_index] = list_to_sort[end_index], list_to_sort[middle]

    # Przeszukiwanie indeksami i, j element??w mniejszych wi??kszych od pivota i zamiana miejsc je??li warunek si?? spe??ni
    #  i-ty indeks przeszukuje element??w mniejszych od pivota do przedostatniego elementu tablicy, bo tam jest nasz
    #  pivot przerzucony
    j = start_index
    for i in range(j, end_index):
        if list_to_sort[i] < pivot:
            list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]
            j += 1

    # Przywr??cenie pivota na poprawn?? pozycj?? w li??cie pod j-tym elementem (tam by??a ostatnia zmiana)
    list_to_sort[end_index], list_to_sort[j] = list_to_sort[j], list_to_sort[end_index]

    # Wywo??anie quick sort do podzielonych tablic -> pivot nie wchodzi w podzia??, bo znajduje si?? na odpowiedniej
    # pozycji, mniejsze s?? po lewej stronie, wi??ksze po prawej
    if start_index < j - 1:
        quick_sort(list_to_sort, start_index, j - 1)
    if j + 1 < end_index:
        quick_sort(list_to_sort, j + 1, end_index)


def select_sort(list_to_sort):
    n = len(list_to_sort)
    for i in range(n):
        for j in range(i + 1, n):
            if list_to_sort[i] > list_to_sort[j]:
                list_to_sort[i], list_to_sort[j] = list_to_sort[j], list_to_sort[i]


def timsort(list_to_sort):
    return sorted(list_to_sort)


def heap_sort(list_to_sort):
    from heapq import heappop, heappush
    my_heap = []
    for value in list_to_sort:
        heappush(my_heap, value)
    return [heappop(my_heap) for i in range(len(my_heap))]


def random_sorting_alghorithm_time(n, name_of_function):
    SETUP_CODE = f'''
from random import randint
from sorting import {name_of_function}, prepare_data

random_list, sorted_list, sorted_reversed_list, sorted_with_one_change = prepare_data({n})'''

    TEST_CODE_RANDOM = f'''
{name_of_function}(random_list)'''
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE_RANDOM,
                          repeat=3,
                          number=100)
    return sum(times) / len(times)


def alghorithm_time(n, name_of_function):
    SETUP_CODE = f'''
from random import randint
from sorting import {name_of_function}, prepare_data

random_list, sorted_list, sorted_reversed_list, sorted_with_one_change = prepare_data({n})'''

    TEST_CODE_RANDOM = f'''
{name_of_function}(random_list)'''

    TEST_CODE_SORTED = f'''
{name_of_function}(sorted_list)'''

    TEST_CODE_REVERSED = f'''
{name_of_function}(sorted_reversed_list)'''

    TEST_CODE_ONE_CHANGE = f'''
{name_of_function}(sorted_with_one_change)'''
    print(f'Testing function: {name_of_function} for {n} elements:')
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE_RANDOM,
                          repeat=3,
                          number=100)
    print(f'Random sorting: {sum(times) / len(times)}')

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE_SORTED,
                          repeat=3,
                          number=100)
    print(f'Sorted sorting: {sum(times) / len(times)}')

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE_REVERSED,
                          repeat=3,
                          number=100)
    print(f'Reversed sorting: {sum(times) / len(times)}')

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE_ONE_CHANGE,
                          repeat=3,
                          number=100)
    print(f'One-change sorting: {sum(times) / len(times)}')
    print()

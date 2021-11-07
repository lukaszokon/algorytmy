from random import randint


def prepare_data(n):
    random_list = []
    for i in range(n):
        random_list.append(randint(1, n * 100))
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


if __name__ == '__main__':
    n = 5
    random_list, sorted_list, sorted_reversed_list, sorted_with_one_change = prepare_data(n)
    print(random_list, sorted_list, sorted_reversed_list, sorted_with_one_change)
    bubble_sort_2(random_list)
    bubble_sort_2(sorted_list)
    bubble_sort_2(sorted_reversed_list)
    bubble_sort_2(sorted_with_one_change)
    print(random_list, sorted_list, sorted_reversed_list, sorted_with_one_change)

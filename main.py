from random import randint


def prepare_data(n):
    random_list = []
    for i in range(n):
        random_list.append(randint(1, n * 100))
    sorted_list = sorted(random_list)
    sorted_reversed_list = sorted_list[::-1]
    sorted_with_one_change = sorted_list

    # mid_index = n//2
    # temp_number = sorted_with_one_change[mid_index]
    # sorted_with_one_change[mid_index] = sorted_with_one_change[mid_index- 1]
    # sorted_with_one_change[mid_index - 1] = temp_number

    sorted_with_one_change[n // 2], sorted_with_one_change[n // 2 - 1] = sorted_with_one_change[n // 2 - 1], \
                                                                         sorted_with_one_change[n // 2]

    return random_list, sorted_list, sorted_reversed_list, sorted_with_one_change



def bubble_sort(list_to_sort):
    pass


if __name__ == '__main__':
    n = 1000
    random_list, sorted_list, sorted_reversed_list, sorted_with_one_change = prepare_data(n)

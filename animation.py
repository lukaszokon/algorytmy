import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib as mp

from sorting import bubble_sort_3, prepare_data, select_sort, insert_sort

TEXT = None


def animate(A, rects, iteration):
    for rect, val in zip(rects, A):
        rect.set_height(val)

    iteration[0] += 1
    TEXT.set_text("iterations : {}".format(iteration[0]))


def init(n):
    global TEXT
    random_list, sorted_list, sorted_reversed_list, sorted_with_one_change = prepare_data(n)
    # to set the colors of the bars.

    generator = insert_sort(random_list)

    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map",
        {
            "red": [(0, 1.0, 1.0),
                    (1.0, .5, .5)],
            "green": [(0, 0.5, 0.5),
                      (1.0, 0, 0)],
            "blue": [(0, 0.50, 0.5),
                     (1.0, 0, 0)]
        }
    )

    fig, ax = plt.subplots()

    # the bar container
    rects = ax.bar(range(len(random_list)), random_list, align="edge",
                   color=color_map(data_normalizer(range(n))))

    # setting the view limit of x and y axes
    ax.set_xlim(0, len(random_list))
    ax.set_ylim(0, int(1.1 * len(random_list)))

    # the text to be shown on the upper left
    # indicating the number of iterations
    # transform indicates the position with
    # relevance to the axes coordinates.
    TEXT = ax.text(0.01, 0.95, "", transform=ax.transAxes)
    iteration = [0]

    anim = FuncAnimation(fig, func=animate,
                         fargs=(rects, iteration), frames=generator, interval=50,
                         repeat=False)

    plt.show()




def visualize_tests():
    from sorting import random_sorting_alghorithm_time
    lengths = [10, 100, 200, 400, 600, 800, 1000, 1200, 1500, 1700, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
    quick_sort_results = []
    timsort_results = []
    bubble_sort_results = []
    for length in lengths:
        quick_sort_results.append(random_sorting_alghorithm_time(length,'quick_sort_init'))
        bubble_sort_results.append(random_sorting_alghorithm_time(length, 'bubble_sort_3'))
        timsort_results.append(random_sorting_alghorithm_time(length, 'timsort'))
    plt.plot(lengths, quick_sort_results, label='quick')
    plt.plot(lengths, bubble_sort_results, label='bubble_3')
    plt.plot(lengths, timsort_results, label='timsort')
    plt.legend()
    plt.show()

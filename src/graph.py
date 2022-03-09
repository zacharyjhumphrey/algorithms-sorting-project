from backend import bubble_sort, create_random_array, merge_sort, pancake_sort, quick_sort, time_sorting_fn
import matplotlib.pyplot as plt

# TODO Need to pass in x and y values
# TODO What is the best graph type for our purposes
"""
TODO I think we should have two 'types' of graphs: one graph that shows how one sorting algorithm 
fairs against each of the test cases and another where we see how one sorting algorithm fairs against
each of the different test cases. this would lead to n*m graphs with n being the number of sorting
algorithms and m being the different test cases
"""


def create_graph(arr, title):
    X_AXIS_LABEL = 'SORTING FUNCTIONS'
    ARRAY_SIZES = [10, 100, 200]

    figure, axis = plt.subplots(len(ARRAY_SIZES), 1)

    # x axis values
    x = ['bubble sort', 'pancake sort', 'quick sort', 'merge sort']
    sorting_data = {
        bubble_sort: {}, pancake_sort: {}, quick_sort: {}, merge_sort: {}
    }

    # TODO 1000 returns call stack error
    for i, size in enumerate(ARRAY_SIZES):
        for fn, data in sorting_data.items():
            data[size] = time_sorting_fn(fn, arr, 1)
        # plotting the points
        axis[i].bar(x, [data[size] for key, data in sorting_data.items()])
        axis[i].set_ylabel(f'{size} ELEMENTS')

    plt.xlabel(X_AXIS_LABEL)
    axis[0].set_title(title)

    # function to show the plot
    plt.show()

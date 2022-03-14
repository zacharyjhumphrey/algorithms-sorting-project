import random
from time import time
import timeit
from typing import Callable, Tuple

MIN_RANDOM_VALUE_RANGE = 1
MAX_RANDOM_VALUE_RANGE = 10000000000
DEFAULT_ARRAY_SIZE = 8


def pancake_sort(arr: list[int]) -> list[int]:
    """
    pancake_sort _summary_

    Args:
        arr (list[int]): array to sort

    Returns:
        list[int]: sorted array
    """

    if len(arr) <= 1:
        return arr

    for size in range(len(arr), 1, -1):
        maxindex = max(range(size), key=arr.__getitem__)
        if maxindex+1 != size:
            # This indexed max needs moving
            if maxindex != 0:
                # Flip the max item to the left
                arr[:maxindex+1] = reversed(arr[:maxindex+1])
            # Flip it into its final position
            arr[:size] = reversed(arr[:size])
    return arr
# https://rosettacode.org/wiki/Sorting_algorithms/Pancake_sort#Python

def bubble_sort(arr: list[int]) -> list[int]:
    """
    bubble_sort _summary_

    Args:
        arr (list[int]): _description_

    Returns:
        list[int]: _description_
    """

    changed = True
    while changed:
        changed = False

        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                changed = True
    return arr
# https://rosettacode.org/wiki/Sorting_algorithms/Bubble_sort#Python

def partition(array,low,high):
    i = ( low - 1 )
    x = array[high]
 
    for j in range(low , high):
        if   array[j] <= x:
 
            i = i+1
            array[i],array[j] = array[j],array[i]
 
    array[i+1],array[high] = array[high],array[i+1]
    return (i+1)

def quick_sort(arr: list[int]) -> list[int]:
    """
    quick_sort _summary_

    Args:
        arr (list[int]): array to sort

    Returns:
        list[int]: sorted array
    """

    high = len(arr) - 1
    low = 0

    #  auxiliary stack
    size = high - low + 1
    stack = [0] * (size)
 
    top = -1
 
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = high
 
    # Keep popping from stack while is not empty
    while top >= 0:
 
        # Pop high and low
        high = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1
 
        # sorted array
        p = partition(arr, low, high )

        # push left side to stack
        if p-1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        #  push right side to stack
        if p+1 < high:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = high

    return arr
# https://www.studytonight.com/python-programs/python-program-for-iterative-quicksort

def merge(a, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = a[l + i]
    for i in range(0, n2):
        R[i] = a[m + i + 1]
 
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1
 
    while i < n1:
        a[k] = L[i]
        i += 1
        k += 1
 
    while j < n2:
        a[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr: list[int]) -> list[int]:
    """
    merge_sort _summary_

    Args:
        arr (list[int]): array to sort

    Returns:
        list[int]: sorted array
    """
     # start with least partition size of 2^0 = 1
    width = 1   
    n = len(arr)                                         
    # subarray size grows by powers of 2
    # since growth of loop condition is exponential,
    # time consumed is logarithmic (log2n)
    while (width < n):
        # always start from leftmost
        l=0
        while (l < n):
            r = min(l+(width*2-1), n-1)        
            m = min(l+width-1,n-1)
            # final merge should consider
            # unmerged sublist if input arr
            # size is not power of 2             
            merge(arr, l, m, r)
            l += width*2
        # Increasing sub array size by powers of 2
        width *= 2
    return arr
# https://www.geeksforgeeks.org/iterative-merge-sort/

def time_sorting_fn(sorting_fn: Callable[[list[int]], list[int]], arr: list[int], repeat: int = 1000) -> int:
    """
    time_sort takes a function and an array and returns how long it took
    for that array to be sorted

    Args:
        sorting_fn (Callable[[list[int]], list[int]]): sorting function to use
        arr (list[int]): array to sort

    Returns:
        int: amount of time it took to sort
    """
    return timeit.timeit(lambda: sorting_fn(arr), number=repeat)


def create_sorted_array_with_one_mistake(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    """
    create_sorted_array_with_one_swap makes an array that only has one value out of place
    example: [1, 2, 7, 3, 4]
    in this case, 7 is out of place, but moving it to the end of the array will 
    easily sort the array
    TODO Make methods similar to this but they have smaller elements or something
    TODO Code review

    Args:
        size (int, optional): size of the array . Defaults to DEFAULT_ARRAY_SIZE.

    Returns:
        list[int]: _description_
    """
    sorted_array = sorted(create_random_array())
    (pos_to_grab, pos_to_insert_into) = random.sample(
        range(0, len(sorted_array)), 2)
    grabbed_elem = sorted_array.pop(pos_to_grab)
    sorted_array.insert(pos_to_insert_into, grabbed_elem)
    return sorted_array


def create_reversed_array(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    """
    create_reversed_array creates a list of numbers that is sorted in descending order

    Args:
        size (int): size of the array

    Returns:
        list[int]: sorted array
    """
    return list(reversed(sorted(create_random_array(size))))


def create_sorted_array(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    return list(sorted(create_random_array(size)))


def create_array_of_one_value(size: int = DEFAULT_ARRAY_SIZE, single_value: int = random.random()) -> list[int]:
    return [single_value] * size


def create_random_array(size: int = DEFAULT_ARRAY_SIZE) -> list[int]:
    return random.sample(range(MIN_RANDOM_VALUE_RANGE, MAX_RANDOM_VALUE_RANGE), size)

# TODO Think of more cases that we should look for when sorting arrays

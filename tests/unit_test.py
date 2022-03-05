from backend import *
import random


def test_pancake_sort():
    arr = random.sample(range(10, 30), 5)
    assert sorted(arr) == pancake_sort(arr)


def test_bubble_sort():
    arr = random.sample(range(10, 30), 5)
    assert sorted(arr) == bubble_sort(arr)


def test_quick_sort():
    arr = random.sample(range(10, 30), 5)
    assert sorted(arr) == quick_sort(arr)


def test_merge_sort():
    arr = random.sample(range(10, 30), 5)
    assert sorted(arr) == merge_sort(arr)


def test_create_sorted_array():
    arr = create_sorted_array()
    assert sorted(arr) == arr
    failing_arr = [3, 4, 5, 12, 9]
    assert sorted(failing_arr) != failing_arr


def test_create_reversed_array():
    arr = create_reversed_array()
    assert sorted(arr) == list(reversed(arr))
    failing_arr = [3, 4, 8, 5]
    assert sorted(failing_arr) != list(reversed(failing_arr))


def test_create_array_of_one_value():
    arr = create_array_of_one_value()
    single_value = arr[0]
    assert all(map(lambda x: x == single_value, arr))

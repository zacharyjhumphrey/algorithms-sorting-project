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


def test_create_reversed_array():
    arr = create_reversed_array()
    assert sorted(arr) == reversed(arr)

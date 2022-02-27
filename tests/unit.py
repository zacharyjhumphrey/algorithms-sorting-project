from backend import pancake_sort
import random

def test_pancake_sort():
    arr = random.sample(range(10, 30), 5)
    assert pancake_sort()
import pytest

from main.leetcode.learn.sorting.problem4434 import Problem4434

def test_base():
    solution = Problem4434()
    lst = [7,3,2,1,5,6,10, 9,8]
    assert solution.bubble_sort(lst) == [1, 2, 3, 5, 6, 7, 8, 9, 10]
import pytest

from main.leetcode.learn.sorting.problem4484 import Problem4484

def test_base():
    solution = Problem4484()
    heights = [5,1,2,3,4]
    assert solution.heightChecker(heights) == 5
import pytest 

from main.leetcode.learn.sorting.problem4483 import Problem4483

def test_base():
    solution = Problem4483()
    nums = [2,0,2,1,1,0]
    assert solution.sortColors(nums) == [0,0,1,1,2,2]



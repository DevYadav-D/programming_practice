import pytest
from main.leetcode.learn.arrays.problem3237 import Problem3237

def test_base():
    solution = Problem3237()
    nums = nums = [12,345,2,6,7896]
    assert solution.findNumbers(nums) == 2
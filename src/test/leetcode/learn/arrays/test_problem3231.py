import pytest 

from main.leetcode.learn.arrays.problem3231 import Problem3231

def test_base():
    solution = Problem3231()
    nums = [3,2,1]
    output = 1
    assert solution.thirdMax(nums) == output
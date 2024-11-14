import pytest 

from main.leetcode.learn.arrays.problem1147 import Problem1147

def test_base():
    solution = Problem1147()
    nums = [3,6,1,0]
    output = 1
    assert solution.dominantIndex(nums) == output
import pytest

from main.leetcode.learn.arrays.problem3247 import Problem3247

def test_base():
    solution = Problem3247()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    output = 5
    assert solution.removeElement(nums, val) == output
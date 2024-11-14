import pytest 

from main.leetcode.learn.arrays.problem3228 import Problem3228

def test_base():
    solution = Problem3228()
    heights = [1,1,4,2,1,3]
    output = 3
    assert solution.heightChecker(heights) == output
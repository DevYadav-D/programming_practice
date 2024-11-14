import pytest 

from main.leetcode.learn.arrays.problem1148 import Problem1148

def test_base():
    solution = Problem1148()
    digits = [4,3,2,1]
    output = [4,3,2,2]
    assert solution.plusOne(digits) == output
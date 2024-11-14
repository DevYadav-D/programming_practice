import pytest 

from main.leetcode.learn.arrays.problem1167 import Problem1167

def test_base():
    solution = Problem1167()
    mat = [[1,2],[3,4]]
    output = [1,2,3,4]
    assert solution.findDiagonalOrder(mat) == output
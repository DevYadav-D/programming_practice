import pytest 

from main.leetcode.learn.arrays.problem1168 import Problem1168


def test_base():
    solution = Problem1168()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    output = [1,2,3,6,9,8,7,4,5]
    assert solution.spiralOrder(matrix) == output

def test_base2():
    solution = Problem1168()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    output = [1,2,3,4,8,12,11,10,9,5,6,7]
    assert solution.spiralOrder(matrix) == output
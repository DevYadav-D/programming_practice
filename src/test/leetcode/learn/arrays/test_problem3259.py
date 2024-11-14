import pytest 

from main.leetcode.learn.arrays.problem3259 import Problem3259

def test_base():
    solution = Problem3259()
    arr = [17,18,5,4,6,1]
    output = [18,6,6,6,1,-1]
    assert solution.replaceElements(arr) == output
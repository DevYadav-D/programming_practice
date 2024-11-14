import pytest 

from main.leetcode.learn.arrays.problem3250 import Problem3250

def test_base():
    solution = Problem3250()
    arr = [10,2,5,3]
    output = True
    assert solution.checkIfExist(arr) == output
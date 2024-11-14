import pytest 

from main.leetcode.learn.arrays.problem3251 import Problem3251

def test_base():
    solution = Problem3251()
    arr = [2,1]
    output = False
    assert solution.validMountainArray(arr) == output
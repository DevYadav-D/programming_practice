import pytest

from main.leetcode.learn.arrays.problem3245 import Problem3245

def test_base():
    solution = Problem3245()
    arr = [1,0,2,3,0,4,5,0]
    assert solution.duplicateZeros(arr) == [1,0,0,2,3,0,0,4]
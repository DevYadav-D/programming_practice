import pytest 

from main.leetcode.learn.arrays.problem1144 import Problem1144

def test_base():
    solution = Problem1144()
    nums = [2,1,-1]
    output = 0
    assert solution.pivotIndex(nums) == output

def test_base2():
    solution = Problem1144()
    nums = [1,7,3,6,5,6]
    output = 3
    assert solution.pivotIndex(nums) == output
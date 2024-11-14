import pytest

from main.leetcode.learn.arrays.problem3240 import Problem3240

def test_base():
    solution = Problem3240()
    nums = [-4,-1,0,3,10]
    assert solution.sortedSquares(nums) == [0,1,9,16,100]
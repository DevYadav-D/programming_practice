import pytest 

from main.leetcode.learn.arrays.problem3248 import Problem3248

def test_base():
    solution = Problem3248()
    nums = [1,1,2]
    output = 2
    #output nums = [1,2,2]
    assert solution.removeDuplicates(nums) == output
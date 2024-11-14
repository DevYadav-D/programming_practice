import pytest

from main.leetcode.learn.arrays.problem3253 import Problem3253

def test_base():
    solution = Problem3253()
    nums1 = [1,2,3,0,0,0] 
    m = 3 
    nums2 = [2,5,6] 
    n = 3
    assert solution.merge(nums1, m, nums2, n) == [1,2,2,3,5,6]
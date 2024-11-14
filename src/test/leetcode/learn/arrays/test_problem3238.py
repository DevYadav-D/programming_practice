import pytest
from main.leetcode.learn.arrays.problem3238 import Problem3238

def test_all_ones():
    solution = Problem3238()
    nums = [1,1,1,1,1]
    assert solution.findMaxConsecutiveOnes(nums) == 5

def test_all_zeros():
    solution = Problem3238()
    nums = [0, 0, 0, 0, 0]
    assert solution.findMaxConsecutiveOnes(nums) == 0

def test_mixed_ones_and_zeros():
    solution = Problem3238()
    nums = [1, 1, 0, 1, 1, 1, 0, 1]
    assert solution.findMaxConsecutiveOnes(nums) == 3

def test_single_one():
    solution = Problem3238()
    nums = [0, 0, 1, 0, 0]
    assert solution.findMaxConsecutiveOnes(nums) == 1

def test_multiple_groups_of_ones():
    solution = Problem3238()
    nums = [1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
    assert solution.findMaxConsecutiveOnes(nums) == 3

def test_empty_list():
    solution = Problem3238()
    nums = []
    assert solution.findMaxConsecutiveOnes(nums) == 0
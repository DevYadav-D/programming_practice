import pytest 

from main.leetcode.learn.arrays.problem1183 import Problem1183

def test_base():
    solution = Problem1183()
    s = ["h","e","l","l","o"]
    output = ["o","l","l","e","h"]
    assert solution.reverseString(s) == output

def test_base2():
    solution = Problem1183()
    s = ["H","a","n","n","a","h"]
    assert solution.reverseString(s) == ["h","a","n","n","a","H"]
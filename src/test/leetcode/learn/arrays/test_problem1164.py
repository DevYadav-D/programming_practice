import pytest 

from main.leetcode.learn.arrays.problem1164 import Problem1164

def test_base():
    solution = Problem1164()
    s = "   the sky is blue   "
    output = "blue is sky the"
    assert solution.reverseWords(s) == output
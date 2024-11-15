import pytest 

from main.leetcode.learn.arrays.problem1160 import Problem1160

def test_base():
    solution = Problem1160()
    a = "1111"#"1010"#"11"
    b = "1111"#"1011"#"1"
    output = "11110"
    assert solution.addBinary(a,b) == output
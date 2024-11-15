'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Problem1160(object):
    def addBinary(self, a, b):
        output = ""
        carry = "0"
        size = max(len(a), len(b))
        if len(a)>len(b):
            for i in range(len(a)-len(b)):
                b = "0" + b
        elif len(a)<len(b):
            for i in range(len(b)-len(a)):
                a = "0" + a
        for i in range(size-1,-1,-1):
            if a[i]== "0" and b[i] == "0":
                if carry == "0":
                    output = "0"+output
                else:
                    output = "1" + output
                    carry = "0"
            elif a[i] == "1" and b[i] == "1":
                if carry == "0":
                    output = "0" + output
                    carry = "1"
                else:
                    output = "1" + output
                    carry = "1"
            else:
                if carry == "0":
                    output = "1" + output
                else:
                    output = "0" + output
                    carry = "1"
        print(output)
        if carry == "0":
            return output
        else:
            output = "1"+output   
        print(output)             
        return output

if __name__=="__main__":
    solution = Problem1160()
    a = "1111"#"1010"#"11"
    b = "1111"#"1011"#"1"
    # output = "100"
    # assert solution.addBinary(a,b) == output
    print(solution.addBinary(a,b))

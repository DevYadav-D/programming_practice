'''
Diagonal Traverse

Solution
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
'''

class Problem1167(object):
    def findDiagonalOrder(self, mat):
        row = len(mat)
        col = len(mat[0])
        output = []
        cur_row = cur_col = 0
        going_up = True

        while len(output) != row*col:
            if going_up:
                while cur_row >= 0 and cur_col < col:
                    output.append(mat[cur_row][cur_col])
                    cur_row -= 1
                    cur_col += 1
                if cur_col == col:
                    cur_col -= 1
                    cur_row += 2
                else:
                    cur_row += 1
                going_up = False
            else:
                while cur_row < row and cur_col >= 0:
                    output.append(mat[cur_row][cur_col])
                    cur_row += 1
                    cur_col -= 1
                if cur_row==row:
                    cur_row -= 1
                    cur_col += 2
                else:
                    cur_col += 1
                going_up = True
        return output

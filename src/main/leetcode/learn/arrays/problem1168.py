'''
Spiral Matrix

Solution
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
'''
class Problem1168(object):
    def spiralOrder(self, matrix):
        output = []
        rows = len(matrix)
        cols = len(matrix[0])
        cur_row = cur_col = 0
        going_up = going_down = going_left = False
        going_right = True
        round = 0
        while len(output) != rows*cols:
            if going_right:
                while cur_col < cols-round:
                    output.append(matrix[cur_row][cur_col])
                    cur_col += 1
                cur_row += 1
                cur_col -= 1

                going_right = False
                going_down = True
            elif going_down:
                while cur_row < rows-round:
                    output.append(matrix[cur_row][cur_col])
                    cur_row += 1
                cur_row -= 1
                cur_col -= 1
                going_down = False
                going_left = True
            elif going_left:
                while cur_col >= round:
                    output.append(matrix[cur_row][cur_col])
                    cur_col -= 1
                cur_row -= 1
                cur_col += 1
                going_left = False
                going_up = True
                round += 1
            elif going_up:
                while cur_row >= round:
                    output.append(matrix[cur_row][cur_col])
                    cur_row -= 1
                cur_row += 1
                cur_col += 1
                going_up = False
                going_right = True             
                
        return output
    
if __name__ == "__main__":
    solution = Problem1168()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]#[[1,2,3],[4,5,6],[7,8,9]]
    print(solution.spiralOrder(matrix))
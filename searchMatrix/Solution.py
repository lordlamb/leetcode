"""
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        line_num = len(matrix)
        if line_num == 0:
            return False

        row = 0
        col = 0

        while row < line_num:
            line = matrix[row]
            col_len = len(line)
            if col_len == 0:
                row += 1
            else:
                col = col if col > 0 else col_len - 1
                if line[col] == target:
                    return True
                elif line[col] < target:
                    row += 1
                else:
                    while col >= 0:
                        if line[col] > target:
                            col -= 1
                        elif line[col] == target:
                            return True
                        else:
                            break
                    row += 1

        return False

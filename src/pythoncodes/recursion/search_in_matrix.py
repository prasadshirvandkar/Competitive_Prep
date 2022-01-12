from typing import List


class Solution:
    def search(self, matrix, r, c, target):
        if r < 0 or c >= len(matrix[0]):
            return False

        if matrix[r][c] == target:
            return True

        if matrix[r][c] > target:
            if self.search(matrix, r - 1, c, target):
                return True
        else:
            if self.search(matrix, r, c + 1, target):
                return True

        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.search(matrix, len(matrix) - 1, 0, target)


if __name__ == '__main__':
    s = Solution()
    mat = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    mat1 = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
    print(s.searchMatrix(mat1, 20))

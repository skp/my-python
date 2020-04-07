from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or len(matrix) < 1:
            return None
        start, end = matrix[0][0], matrix[len(matrix) - 1][len(matrix) - 1]

        def notGreaterCount(matrix: List[List[int]], n: int) -> int:
            _row = len(matrix)
            _col = len(matrix[0])
            _lastCol = _col - 1
            curRow = 0
            cnt = 0
            while curRow < _row:
                for j in range(_lastCol, -1, -1):
                    if matrix[curRow][j] <= n:
                        cnt += (j + 1)
                        break
                curRow += 1
            return cnt

        while start < end:
            mid = start + ((end - start) >> 1)
            cnt = notGreaterCount(matrix, mid)
            if cnt < k:
                start = mid + 1
            else:
                end = mid
        return mid


if __name__ == '__main__':
    # matrix =
    Solution().kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8)

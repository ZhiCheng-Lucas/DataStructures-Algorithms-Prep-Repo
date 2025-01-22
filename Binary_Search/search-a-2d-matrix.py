class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Performs a two-stage binary search on a sorted matrix to find a target value.
        The matrix has two special properties:
        1. Each row is sorted in ascending order
        2. First element of each row is greater than last element of previous row

        Approach:
        1. First binary search: Find the correct row that might contain target
        2. Second binary search: Search within that row for the target

        Time complexity: O(log(m*n)) where m = rows, n = columns
        Space complexity: O(1) as we only use pointers
        """

        # First binary search to find the potential row
        row_start = 0
        row_end = len(matrix) - 1

        while row_start <= row_end:
            row_mid = (row_start + row_end) // 2

            # If target is less than first element of row, search upper half
            if target < matrix[row_mid][0]:
                row_end = row_mid - 1

            # If target is greater than last element of row, search lower half
            elif target > matrix[row_mid][-1]:
                row_start = row_mid + 1

            # Target might be in current row, perform second binary search
            else:
                # Second binary search within the identified row
                col_start = 0
                col_end = len(matrix[row_mid]) - 1

                while col_start <= col_end:
                    col_mid = (col_start + col_end) // 2

                    if target == matrix[row_mid][col_mid]:
                        return True

                    if target > matrix[row_mid][col_mid]:
                        col_start = col_mid + 1
                    else:
                        col_end = col_mid - 1

                return False

        return False

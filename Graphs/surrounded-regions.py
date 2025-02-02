class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Captures surrounded regions in a board of X's and O's by converting
        surrounded O's to X's. A region is considered surrounded if it's completely
        enclosed by X's and not connected to the board's border.

        Strategy:
        Instead of finding surrounded regions directly, we identify regions that
        CAN'T be captured - those connected to the border. Any remaining O's
        must be surrounded.

        1. Find all 'O's on the border
        2. Use DFS to mark all 'O's connected to border as 'Z' (safe zones)
        3. Convert remaining 'O's to 'X's (they're surrounded)
        4. Restore 'Z's back to 'O's (these were safe)

        Time: O(m*n) - visit each cell at most once
        Space: O(m*n) - recursive stack in worst case of all O's
        """
        if not board or not board[0]:
            return

        rows = len(board)
        cols = len(board[0])

        def mark_safe_region(row: int, col: int) -> None:
            """
            DFS to mark all 'O' cells connected to a safe cell (border-connected)
            by converting them to 'Z' temporarily.
            """
            # Out of bounds or not an 'O' cell
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != "O":
                return

            # Mark current cell as safe
            board[row][col] = "Z"

            # Check all adjacent cells
            mark_safe_region(row + 1, col)
            mark_safe_region(row - 1, col)
            mark_safe_region(row, col + 1)
            mark_safe_region(row, col - 1)

        # Phase 1: Mark all border-connected regions as safe
        # Check first and last row
        for col in range(cols):
            if board[0][col] == "O":
                mark_safe_region(0, col)
            if board[rows - 1][col] == "O":
                mark_safe_region(rows - 1, col)

        # Check first and last column
        for row in range(rows):
            if board[row][0] == "O":
                mark_safe_region(row, 0)
            if board[row][cols - 1] == "O":
                mark_safe_region(row, cols - 1)

        # Phase 2: Capture surrounded regions and restore safe regions
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":  # Surrounded O found
                    board[row][col] = "X"
                elif board[row][col] == "Z":  # Safe O found
                    board[row][col] = "O"

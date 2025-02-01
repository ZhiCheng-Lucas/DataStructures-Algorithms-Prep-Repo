class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Fills each land cell with its shortest distance to the nearest treasure chest using BFS.

        Strategy:
        1. Start BFS simultaneously from all treasure chests (value 0)
        2. For each cell, propagate distance to unvisited neighboring land cells
        3. Water cells (-1) block the path and can't be traversed

        Time: O(m*n) - visits each cell at most once
        Space: O(m*n) - queue can contain at most all cells in worst case
        """
        rows = len(grid)
        columns = len(grid[0])
        INF = 2147483647
        queue = deque()

        # Collect coordinates of all treasure chests as starting points
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 0:  # Found a treasure chest
                    queue.append([row, column])

        # Possible movements: down, up, right, left
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # BFS from all treasure chests simultaneously
        while queue:
            curr_row, curr_col = queue.popleft()

            # Explore all four adjacent cells
            for delta_row, delta_col in directions:
                next_row = curr_row + delta_row
                next_col = curr_col + delta_col

                # Skip if out of bounds
                if next_row < 0 or next_col < 0 or next_row >= rows or next_col >= columns:
                    continue

                # If we find an unvisited land cell, update its distance
                if grid[next_row][next_col] == INF:
                    grid[next_row][next_col] = grid[curr_row][curr_col] + 1
                    queue.append([next_row, next_col])

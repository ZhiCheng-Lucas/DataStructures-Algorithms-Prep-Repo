class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Number of Islands - Using DFS to sink connected land masses

        Strategy:
        When we encounter a piece of land ('1'), we:
        1. Increment our island count
        2. Use DFS to explore and "sink" the entire island (convert connected '1's to '0's)
        3. This ensures we count each island exactly once

        Time Complexity:  O(m × n) - we visit each cell once
        Space Complexity: O(m × n) - in worst case of all land, recursion stack can go up to m × n
        """
        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def sink_island(row, col):
            # Stop if out of bounds or if we hit water
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return

            # Sink current land cell
            grid[row][col] = "0"

            # Recursively sink all adjacent land cells
            # Check all 4 directions: up, down, left, right
            sink_island(row + 1, col)
            sink_island(row - 1, col)
            sink_island(row, col - 1)
            sink_island(row, col + 1)

        # Scan the grid looking for islands
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_count += 1
                    sink_island(row, col)  # Sink the entire island

        return island_count

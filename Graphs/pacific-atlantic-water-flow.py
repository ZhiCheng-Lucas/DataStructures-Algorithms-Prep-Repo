class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Strategy:
        1. Start DFS from the borders of both oceans separately
        2. For Pacific: Start from top and left edges
        3. For Atlantic: Start from bottom and right edges
        4. Water can flow from higher/equal elevation to lower
        5. Return cells that can reach both oceans

        Time Complexity: O(m*n) where m and n are dimensions of the grid
        Space Complexity: O(m*n) for the visited sets
        """
        rows = len(heights)
        cols = len(heights[0])

        # Track cells that can reach each ocean
        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row, col, visited, prev_height):
            """
            DFS to mark all cells that water can flow from to the current cell
            Water flows from higher/equal elevation to lower elevation
            """
            # Check bounds and if already visited
            if (
                row < 0
                or col < 0
                or row >= rows
                or col >= cols
                or (row, col) in visited
                or heights[row][col] < prev_height
            ):
                return

            visited.add((row, col))
            current_height = heights[row][col]

            # Check all 4 directions: down, up, right, left
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dx, dy in directions:
                dfs(row + dx, col + dy, visited, current_height)

        # Start DFS from Pacific borders (top and left)
        for col in range(cols):
            dfs(0, col, pacific_reachable, heights[0][col])
        for row in range(rows):
            dfs(row, 0, pacific_reachable, heights[row][0])

        # Start DFS from Atlantic borders (bottom and right)
        for col in range(cols):
            dfs(rows - 1, col, atlantic_reachable, heights[rows - 1][col])
        for row in range(rows):
            dfs(row, cols - 1, atlantic_reachable, heights[row][cols - 1])

        # Return cells that can reach both oceans (intersection of sets)
        return list(pacific_reachable & atlantic_reachable)

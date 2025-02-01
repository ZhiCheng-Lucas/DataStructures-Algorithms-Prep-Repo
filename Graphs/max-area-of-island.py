class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Strategy:
        Using DFS to explore islands in a binary matrix where 1 represents land and 0 represents water.
        When we find a land cell (1), we explore all its 4-directional neighbors to calculate the total
        area of the connected island. We mark visited cells as 0 to avoid counting them again.

        1. Iterate through each cell in the grid
        2. When land (1) is found, use DFS to explore all connected land cells
        3. Keep track of the maximum area found so far
        4. Mark visited cells as 0 to avoid revisiting them

        Time Complexity:  O(m × n) where m and n are the dimensions of the grid
        Space Complexity: O(m × n) worst case for the recursion stack when the entire grid is land

        """

        rows = len(grid)
        columns = len(grid[0])
        max_area = 0

        # DFS
        def find_connecting_islands_number(row, column):

            # Base Case
            # Boundary Handling:
            if row >= rows or column >= columns or row < 0 or column < 0:
                return 0

            if grid[row][column] == 0:
                return 0

            # Recursive Call
            grid[row][column] = 0
            connecting_islands = 1

            connecting_islands += find_connecting_islands_number(row + 1, column)  # down
            connecting_islands += find_connecting_islands_number(row - 1, column)  # up
            connecting_islands += find_connecting_islands_number(row, column - 1)  # left
            connecting_islands += find_connecting_islands_number(row, column + 1)  # right

            return connecting_islands

        for row in range(rows):
            for column in range(columns):

                # Island Found.
                if grid[row][column] == 1:
                    area = find_connecting_islands_number(row, column)
                    max_area = max(max_area, area)

        return max_area

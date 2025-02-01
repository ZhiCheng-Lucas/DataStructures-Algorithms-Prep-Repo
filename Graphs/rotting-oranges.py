class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Rotting Oranges - Breadth First Search Solution

        Strategy:
        1. First locate all initially rotten oranges and count fresh ones
        2. Use BFS to simulate the rotting process layer by layer
        3. Each layer represents one minute of time
        4. Process continues until either all oranges are rotten or no more oranges can be reached

        Time Complexity: O(m*n) where m and n are the dimensions of the grid
        Space Complexity: O(m*n) in worst case where all oranges are rotten initially
        """

        rows = len(grid)
        columns = len(grid[0])
        queue = deque()
        minute = 0
        fresh_oranges = 0

        # Find all initial rotten oranges and count fresh ones
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == 2:
                    queue.append([row, column])
                elif grid[row][column] == 1:
                    fresh_oranges += 1

        # Possible movements: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Process rotting layer by layer, where each layer is one minute
        while queue and fresh_oranges > 0:
            # Process all oranges that became rotten in the previous minute
            for _ in range(len(queue)):
                current_row, current_col = queue.popleft()

                # Check all adjacent cells
                for delta_row, delta_col in directions:
                    next_row = current_row + delta_row
                    next_col = current_col + delta_col

                    # Skip if outside grid boundaries
                    if next_row < 0 or next_col < 0 or next_row >= rows or next_col >= columns:
                        continue

                    # If we find a fresh orange, make it rotten and add to queue
                    if grid[next_row][next_col] == 1:
                        grid[next_row][next_col] = 2
                        fresh_oranges -= 1
                        queue.append((next_row, next_col))

            minute += 1

        # Return -1 if any fresh oranges remain, otherwise return elapsed minutes
        return minute if fresh_oranges == 0 else -1

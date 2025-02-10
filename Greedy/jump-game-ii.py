class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Use a level-by-level BFS approach.
        At each level, we determine the furthest index we can reach from current positions.

        Approach:
        - Use two pointers (left, right) to track the current level's range
        - For each position in current level, find furthest reachable index
        - Move to next level by updating pointers and increment step count

        Example walkthrough with [2,3,1,1,4]:
        Level 0: pos 0 (value=2) -> can reach index 1,2
        Level 1: pos 1,2 (values=3,1) -> can reach index 3,4
        Level 2: reached target index 4

        Time complexity: O(n) - visit each position once
        Space complexity: O(1) - only use pointers and variables
        """
        steps = 0  # Track number of jumps taken
        left, right = 0, 0  # Window representing current level positions

        while right < len(nums) - 1:  # Continue until we can reach last index
            furthest_reach = 0  # Track furthest index reachable from current level

            # Check each position in current level
            for curr_pos in range(left, right + 1):
                furthest_reach = max(furthest_reach, curr_pos + nums[curr_pos])

            # Move window to next level
            left = right + 1
            right = furthest_reach
            steps += 1

        return steps

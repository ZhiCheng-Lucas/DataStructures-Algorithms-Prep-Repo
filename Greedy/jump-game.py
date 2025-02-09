class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Jump Game - Greedy Approach from End to Start

        Strategy:
        Instead of finding a path from start to end, we work backwards.
        For each position, we check if we can reach our current target
        from that position. If we can, that position becomes our new target.

        Time Complexity: O(n) - single pass through the array
        Space Complexity: O(1) - only using a single variable
        """
        # Start from the last index as our initial target
        target = len(nums) - 1

        # Iterate backwards through the array
        for i in range(len(nums) - 2, -1, -1):
            # If current position can reach target (current position + max jump >= target),
            # mark this position as the new target
            if nums[i] + i >= target:
                target = i

        # If target reaches index 0, it means we found a valid path from start to end
        return target == 0

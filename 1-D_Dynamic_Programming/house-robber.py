class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        House Robber - Dynamic Programming with Memoization

        At each house, we have two choices:
        1. Rob the current house + max money from houses before previous house
        2. Skip current house and keep max money from previous house

        Recurrence relation:
        dp[n] = max(dp[n-2] + nums[n], dp[n-1])
        where dp[n] represents max money we can rob up to house n

        Example: [2,7,9,3,1]
        dp[0] = 2        # only first house
        dp[1] = 7        # max between first and second house
        dp[2] = 2+9 = 11 # first + third house
        dp[3] = 11       # same as previous (skip house 4)
        dp[4] = 11+1 = 12# dp[2] + last house

        Time Complexity: O(n)
        - Each house is calculated exactly once and stored in memo
        - Subsequent lookups are O(1) from memo

        Space Complexity: O(n)
        - Memoization dictionary stores result for each house
        - Recursive call stack can go up to n depth
        """
        memo = {}

        # Handle edge cases of 1 or 2 houses
        if len(nums) <= 2:
            return max(nums)

        # Initialize base cases
        memo[0] = nums[0]  # Rob first house
        memo[1] = max(nums[1], memo[0])  # Rob either first or second house

        def recursive_call(house_idx):
            # Return cached result if already calculated
            if house_idx in memo:
                return memo[house_idx]

            # For current house, choose maximum between:
            # 1. Rob current house + money from houses before previous
            # 2. Skip current house and keep money from previous house
            memo[house_idx] = max(
                recursive_call(house_idx - 2) + nums[house_idx],  # Rob current
                recursive_call(house_idx - 1),  # Skip current
            )
            return memo[house_idx]

        return recursive_call(len(nums) - 1)

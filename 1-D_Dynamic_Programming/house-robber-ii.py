class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Strategy:
        Since houses are arranged in a circle (first and last houses are adjacent),
        we break this into two subproblems using House Robber I logic:
        1. Rob houses from index 0 to n-2 (excluding last house)
        2. Rob houses from index 1 to n-1 (excluding first house)
        Take the maximum of these two scenarios.

        For each subproblem, we use dynamic programming with memoization where:
        dp[i] represents the maximum money we can rob up to house i
        dp[i] = max(dp[i-1], dp[i-2] + current_house_money)
        - dp[i-1]: skip current house, take previous best
        - dp[i-2] + current_house_money: rob current house + best from two houses back

        Time Complexity: O(n)
        - We solve two subproblems, each requiring O(n) time
        - Each house index is calculated exactly once due to memoization

        Space Complexity: O(n)
        - We use two memoization dictionaries, each storing up to n entries
        - The recursive call stack can go up to O(n) depth
        """
        if len(nums) <= 2:
            return max(nums)

        # Create two subarrays to handle circular nature
        houses_without_last = nums[: len(nums) - 1]  # Exclude last house
        houses_without_first = nums[1:]  # Exclude first house

        # Initialize memoization for both scenarios
        memo_skip_last = {0: houses_without_last[0], 1: max(houses_without_last[0], houses_without_last[1])}

        memo_skip_first = {0: houses_without_first[0], 1: max(houses_without_first[0], houses_without_first[1])}

        def recursive_function(house_idx, memo, houses):
            # Return memoized result if already calculated
            if house_idx in memo:
                return memo[house_idx]

            # Calculate maximum money by either:
            # 1. Skipping current house (take previous best)
            # 2. Taking current house + best result from two houses back
            memo[house_idx] = max(
                recursive_function(house_idx - 1, memo, houses),  # Skip current house
                recursive_function(house_idx - 2, memo, houses) + houses[house_idx],  # Rob current house
            )
            return memo[house_idx]

        # Calculate maximum money for both scenarios and return the better result
        target_idx = len(nums) - 2  # Index of second-to-last house
        return max(
            recursive_function(target_idx, memo_skip_last, houses_without_last),
            recursive_function(target_idx, memo_skip_first, houses_without_first),
        )

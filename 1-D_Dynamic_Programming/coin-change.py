class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Dynamic Programming Solution - Bottom Up Approach

        Strategy:
        Build up the solution for each amount from 0 to target amount.
        For each amount, try using each coin and find the minimum number
        of coins needed.

        dp[amount] = min(dp[amount - coin] + 1) for each coin if amount >= coin

        Time Complexity: O(amount * len(coins))
        Space Complexity: O(amount)

        """
        # Initialize dp array with impossible value (amount + 1)
        # since we can't use more coins than the amount itself
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        # Build solution for each amount from 1 to target
        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if curr_amount >= coin:
                    dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)

        # If value is still amount + 1, no solution was found
        return dp[amount] if dp[amount] != amount + 1 else -1

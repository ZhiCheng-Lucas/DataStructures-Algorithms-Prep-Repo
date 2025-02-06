class Solution:
    def climbStairs(self, n: int) -> int:
        """
        A dynamic programming solution to find the number of distinct ways to climb n stairs,
        taking either 1 or 2 steps at a time.

        Approach:
        - Work backwards from the top (n) to the bottom (0)
        - At each step i, the number of ways to reach the top equals the sum of:
          * Ways from taking 1 step (dp[i+1])
          * Ways from taking 2 steps (dp[i+2])

        Time complexity: O(n) - single pass from n-2 to 0
        Space complexity: O(n) - dp array of size n+1
        """
        if n <= 1:
            return 1

        # Array to store number of ways to reach top from each step
        ways = [0] * (n + 1)
        ways[n] = 1  # Standing at top - 1 way to reach top
        ways[n - 1] = 1  # One step from top - only 1 way possible

        # For each step, calculate ways by combining:
        # - ways if we take 1 step from here (ways[i+1])
        # - ways if we take 2 steps from here (ways[i+2])
        for step in range(n - 2, -1, -1):
            ways[step] = ways[step + 1] + ways[step + 2]

        return ways[0]  # Return total ways from bottom to top


# Recursive solution

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         '''
#         - Each position represents the total ways to reach that step
#         - To reach step n, we can either:
#           1. Take a single step from position (n-1)
#           2. Take a double step from position (n-2)
#         - The total ways for step n is the sum of both possibilities

#         Time Complexity: O(n) - Each step calculated once and stored in memo
#         Space Complexity: O(n) - Memo dictionary + recursion stack
#         '''

#         memo = {}  # Cache to store previously calculated step combinations

#         def rec(steps):
#             # Base cases: only one way to reach 0 or 1 step
#             if steps == 0 or steps == 1:
#                 return 1

#             # Return cached result if already calculated
#             if steps in memo:
#                 return memo[steps]

#             # Current step combinations = combinations from (n-1) + combinations from (n-2)
#             memo[steps] = rec(steps-1) + rec(steps-2)
#             return memo[steps]

#         return rec(n)

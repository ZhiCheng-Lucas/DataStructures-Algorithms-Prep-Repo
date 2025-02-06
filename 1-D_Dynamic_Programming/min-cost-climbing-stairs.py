class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Strategy:
        - Use recursion with memoization to avoid recalculating subproblem
        - At each step, choose the minimum cost between climbing from 1 or 2 steps below
        - The recurrence relation is: dp[n] = min(dp[n-1], dp[n-2]) + cost[n]

        # Memo[i] stores the minimum cost to reach ith step.
        """

        # Cache to store minimum cost to reach each step
        memo = {}

        def recursive_call(step):
            # Return cached result if already calculated
            if step in memo:
                return memo[step]

            # Base cases: first two steps only require their own cost
            if step == 0 or step == 1:
                return cost[step]

            # When we reach beyond the array (top of stairs),
            # there's no cost for the current step
            curr_cost = cost[step] if step < len(cost) else 0

            # Calculate minimum cost by taking minimum of:
            # 1. Cost of reaching from one step below
            # 2. Cost of reaching from two steps below
            # Then add current step's cost
            memo[step] = min(recursive_call(step - 1), recursive_call(step - 2)) + curr_cost
            return memo[step]

        return recursive_call(len(cost))

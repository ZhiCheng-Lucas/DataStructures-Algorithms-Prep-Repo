def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations of numbers that sum to target using backtracking.
    Each number can be used unlimited times.

    Approach:
    - Use DFS/backtracking to explore all possible combinations
    - At each step, we have two choices:
        1. Take the current number again (stay at same index)
        2. Skip the current number (move to next index)
    - When sum equals target, we've found a valid combination
    - When sum exceeds target or we reach end of array, we backtrack

    Time: O(2^target), as we can reuse numbers
    Space: O(target/min(candidates)), max depth of recursion tree
    """
    res = []
    combination = []

    def dfs(i):
        curr_sum = sum(combination)

        # Base cases: exceeded target or reached end of candidates
        if curr_sum >= target or i >= len(candidates):
            if curr_sum == target:
                res.append(combination.copy())  # Found valid combination
            return

        # Decision 1: Include current number again
        combination.append(candidates[i])
        dfs(i)  # Stay at same index since we can reuse numbers

        # Decision 2: Skip current number
        combination.pop()  # Backtrack by removing the number we added
        dfs(i + 1)  # Move to next candidate

    dfs(0)
    return res

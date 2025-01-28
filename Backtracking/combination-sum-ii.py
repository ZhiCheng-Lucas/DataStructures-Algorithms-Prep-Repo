def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    """
    Find unique combinations of numbers that sum to target, using each number at most once.

    Approach:
    - Sort array first to handle duplicates efficiently
    - Use backtracking with DFS to explore combinations
    - For duplicates like [1,1,1], we handle them sequentially to avoid duplicate combinations
    - Skip consecutive duplicates when choosing not to include a number

    Example: candidates = [1,1,2,5,6,7], target = 8
    - Sort first to group duplicates together
    - When we decide not to use a number, skip all its duplicates
    - This ensures combinations like [1,7] appear only once

    Time: O(2^n) - we have two choices for each number
    Space: O(n) - recursion depth at most n
    """
    res = []
    combination = []
    candidates.sort()  # Sort to handle duplicates

    def dfs(i):
        curr_sum = sum(combination)

        # Stop if we exceed target or reach end
        if curr_sum >= target or i >= len(candidates):
            if curr_sum == target:
                res.append(combination.copy())
            return

        # Include current number in combination
        combination.append(candidates[i])
        dfs(i + 1)

        # Skip current number and its duplicates
        combination.pop()
        while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
            i += 1
        dfs(i + 1)

    dfs(0)
    return res

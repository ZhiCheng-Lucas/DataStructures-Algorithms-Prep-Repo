class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible subsets using a backtracking approach.
        
        For each element in nums, we make a binary choice:
        1. Include the current element in the subset
        2. Exclude the current element from the subset
        
        This creates a binary decision tree where:
        - Each level represents a position in nums
        - Left branch: include current number
        - Right branch: exclude current number
        
        Example with [1,2,3]:
                        []
                /              \
            [1]                []
          /      \           /    \
        [1,2]    [1]       [2]    []
        /  \     /  \     /  \    / \
      [123][12][13][1]  [23][2] [3][]
        
        Time complexity: O(2^n) - we make 2 choices for each element
        Space complexity: O(n) - max recursion depth equals array length
        """
        res = []  # Store all valid subsets
        subset = []  # Current subset being built

        def dfs(i):
            # Base case: processed all elements
            if i >= len(nums):
                res.append(subset.copy())  # Add the complete subset
                return

            # Decision 1: Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Decision 2: Exclude nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)  # Start from index 0
        return res

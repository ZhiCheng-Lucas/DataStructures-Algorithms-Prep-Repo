class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible permutations of the input array using recursion.

        Strategy:
        1. Taking the first element of the array
        2. Finding all permutations of the remaining elements recursively
        3. Inserting the first element at every possible position in each permutation

        For example, with [1,2,3]:
        - First, get permutations of [2,3]
            - To get perms of [2,3], first get perms of [3]
            - [3] is base case, returns [[3]]
            - Insert 2 in all positions of [3]: [[2,3], [3,2]]
        - Then insert 1 in all positions of [2,3] and [3,2]:
            - [2,3] -> [[1,2,3], [2,1,3], [2,3,1]]
            - [3,2] -> [[1,3,2], [3,1,2], [3,2,1]]

        Time complexity: O(n!∗n 2)
        Space complexity: O(n!∗n) for the output list.


        """
        result = []

        # Base case: single element array has only one permutation
        if len(nums) == 1:
            return [nums]

        # Get permutations of all elements except the first
        sub_permutations = self.permute(nums[1:])
        first_element = nums[0]

        # For each permutation of the remaining elements
        for perm in sub_permutations:
            # Insert first element at every possible position
            for position in range(len(perm) + 1):
                current_perm = perm.copy()
                current_perm.insert(position, first_element)
                result.append(current_perm)

        return result

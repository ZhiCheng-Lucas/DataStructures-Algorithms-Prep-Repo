class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Performs binary search on a sorted array to find the target value.

        The algorithm repeatedly divides the search interval in half:
        - If the middle element is the target, return its index
        - If the target is less than the middle element, search the left half
        - If the target is greater than the middle element, search the right half

        Time complexity: O(log n) - search space is halved in each iteration
        Space complexity: O(1) - only using pointers
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2  # Calculate middle index

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                # Target is in the left half
                right = mid - 1
            else:
                # Target is in the right half
                left = mid + 1

        return -1  # Target not found in array

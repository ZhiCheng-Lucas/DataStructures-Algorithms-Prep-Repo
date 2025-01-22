class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Find the minimum element in a sorted and rotated array using binary search.

        The array was originally sorted in ascending order, then rotated between 1 and n times.

        Approach:
        1. Compare middle element with rightmost element to determine which half
           contains the minimum value
        2. If mid > right: minimum must be in right half (including mid)
        3. If mid < right: minimum must be in left half (including mid)

        # Example: [3,4,5,6,7,1,2] -> mid(6) > right(2)
        # Example: [6,7,1,2,3,4,5] -> mid(2) < right(5)

        Time complexity: O(log n) - binary search
        Space complexity: O(1) - only using pointers
        """
        min_value = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # If middle element >= right element, minimum is in right half
            if nums[mid] >= nums[right]:
                min_value = min(nums[mid], min_value)
                left = mid + 1
            # If middle element < right element, minimum is in left half
            else:
                min_value = min(nums[mid], min_value)
                right = mid - 1

        return min_value

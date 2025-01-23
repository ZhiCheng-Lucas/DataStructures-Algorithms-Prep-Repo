class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary Search in Rotated Sorted Array

        The array consists of two sorted subarrays after rotation:
        Example: [4,5,6,7,0,1,2] becomes:
            Left subarray: [4,5,6,7] (larger values)
            Right subarray: [0,1,2] (smaller values)

        Strategy:
        1. Determine which subarray the middle element belongs to
        2. Based on the target value and middle element:
           - Determine which subarray could contain the target
           - Adjust search space accordingly

        Time Complexity: O(log n) - Binary Search
        Space Complexity: O(1) - Only using pointers
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            # Check if middle element is in left sorted portion
            if nums[mid] >= nums[right]:
                if nums[mid] < target:
                    # Target must be in right portion
                    left = mid + 1
                else:
                    # Target could be in either portion
                    # If target is larger than leftmost element, it's in left portion
                    # Otherwise, it's in right portion
                    if target >= nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
            # Middle element is in right sorted portion
            else:
                if nums[mid] < target:
                    # If target is smaller than or equal to rightmost element
                    # it's in right portion, otherwise left portion
                    if target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    # Target is smaller than middle element
                    # Must be in left portion
                    right = mid - 1

        return -1

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two Sum II - Input Array Is Sorted

        Approach:
        Since the array is sorted, we can use two pointers.
        - Start with pointers at both ends of the array
        - If sum is too large, decrease right pointer to get a smaller number
        - If sum is too small, increase left pointer to get a larger number

        Alternate approach:
        Use hashmap. However, in that case, the space complexity would be O(n) instead.

        Time complexity: O(n) - single pass through the array
        Space complexity: O(1) - only two pointers used
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                # Adding 1 based on question's requirements
                return [left + 1, right + 1]

            if current_sum > target:
                right -= 1
            else:
                left += 1

        return False

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets in nums that sum to zero.

        Approach:
        1. Sort the array to handle duplicates and enable two-pointer technique
        2. Fix one number (a) and find the other two (b, c) using two pointers
        3. Skip duplicate values of 'a' to avoid duplicate triplets
        4. For each fixed 'a', use two pointers to find pairs (b, c) where b + c = -a

        Time Complexity: O(n²) - One loop for 'a' and two pointers for 'b' and 'c'
        Space Complexity: O(1) - Excluding the space needed for output array
        """
        result_array = []
        sorted_nums = sorted(nums)

        for i, fixed_num in enumerate(sorted_nums):
            # Skip duplicate values for fixed_num to avoid duplicate triplets
            if i > 0 and fixed_num == sorted_nums[i - 1]:
                continue

            # Find pairs that sum to -fixed_num using two pointers (two sum problem)
            target = -fixed_num
            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                current_sum = sorted_nums[left] + sorted_nums[right]

                if current_sum == target:
                    result_array.append([fixed_num, sorted_nums[left], sorted_nums[right]])

                    # Skip duplicate values for left pointer
                    left += 1
                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1

                elif current_sum > target:
                    right -= 1
                else:  # current_sum < target
                    left += 1

        return result_array

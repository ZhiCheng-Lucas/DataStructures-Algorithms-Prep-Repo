class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Using XOR bit manipulation to find the single non-duplicated number.

        Strategy:
        - XOR has two key properties we use here:
          1. a ^ a = 0 (number XOR itself = 0)
          2. a ^ 0 = a (number XOR 0 = number itself)
        - When we XOR all numbers in the array:
          - Paired numbers cancel out to 0
          - The single number remains when XOR'd with 0

        Time: O(n) - single pass through the array
        Space: O(1) - only using one variable regardless of input size
        """
        result = 0
        for num in nums:
            # XOR current number with running result
            # Paired numbers cancel out, leaving only the single number
            result = num ^ result
        return result

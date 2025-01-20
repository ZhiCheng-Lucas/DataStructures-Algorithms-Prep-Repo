class Solution:
    """
    Product of Array Except Self: Calculate products without division.

    Solution approach:
    For each position i, multiply:
    1. Product of all elements to the left
    2. Product of all elements to the right

    Example:
    [1,2,3,4]

    Left products (prefix):
    1  →  1        (nothing to left)
    2  →  1        (1)
    3  →  2        (1 × 2)
    4  →  6        (1 × 2 × 3)

    Right products (suffix):
    1  →  24       (2 × 3 × 4)
    2  →  12       (3 × 4)
    3  →  4        (4)
    4  →  1        (nothing to right)

    Final result at each index:
    [24, 12, 8, 6] = [1×24, 1×12, 2×4, 6×1]

    Time: O(n) - three linear passes through array
    Space: O(n) - two auxiliary arrays for products
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_products = [1] * n
        right_products = [1] * n
        result = [1] * n

        # Build products of elements to the left
        for i in range(n):
            if i > 0:
                left_products[i] = left_products[i - 1] * nums[i - 1]

        # Build products of elements to the right
        for i in range(n - 1, -1, -1):
            if i < n - 1:
                right_products[i] = right_products[i + 1] * nums[i + 1]

        # Combine left and right products
        for i in range(n):
            result[i] = left_products[i] * right_products[i]

        return result

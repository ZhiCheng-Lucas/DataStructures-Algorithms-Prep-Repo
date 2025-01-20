class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Determines if a string is a palindrome after converting to lowercase and removing non-alphanumeric characters.

        Uses a two-pointer technique, comparing characters from both ends moving inward:
        1. Skips non-alphanumeric characters
        2. Compares lowercase versions of valid characters
        3. Returns false if any mismatch is found
        4. Returns true if all comparisons match or the pointers meet in the middle

        Time Complexity: O(n) - each character is visited at most once
        Space Complexity: O(1) - only uses two pointers regardless of input size
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters from left side
            while left < right and not s[left].isalnum():
                left += 1

            # Skip non-alphanumeric characters from right side
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

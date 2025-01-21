class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Find the length of the longest substring without repeating characters using the sliding window approach.

        Strategy:
        - Use two pointers (sliding window) to maintain a window of unique characters
        - Use a hashset to track unique characters in current window
        - When duplicate is found, shrink window from left until duplicate is removed
        - Track maximum window size throughout the process

        Time Complexity: O(n) - each character is processed at most twice
        Space Complexity: O(min(m,n)) where m is the size of character set
        """

        unique_chars = set()
        max_length = 1
        left, right = 0, 1

        # Handle empty string and single character cases
        if len(s) < 2:
            return len(s)

        unique_chars.add(s[left])

        while right < len(s):
            # Expand window if current character is unique
            if s[right] not in unique_chars:
                unique_chars.add(s[right])
                max_length = max(max_length, len(unique_chars))
                right += 1
            # Shrink window from left when duplicate is found
            else:
                unique_chars.remove(s[left])
                left += 1

        return max_length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Find the longest substring with same letter after at most k character replacements.

        Uses sliding window technique with a hashmap to track character frequencies.
        For any valid window:
            window_length - count_of_most_frequent_char <= k

        This means we can replace the non-most-frequent characters (whose total count
        is window_length - max_freq) to match the most frequent character.

        Strategy:
        1. Maintain a sliding window and count characters using hashmap
        2. For each window, check if we can make all chars same using ≤ k replacements
        3. If invalid window, shrink from left. If valid, expand from right

        Time Complexity: O(n)
        - We traverse the string once with the right pointer
        - The left pointer never moves more than n positions total
        - max(char_count.values()) is O(1) since we only have uppercase letters (26 max)

        Space Complexity: O(1)
        - char_count hashmap stores at most 26 uppercase letters
        - All other variables use constant space



        """

        longest_sub = 1
        left, right = 0, 1

        # Track character frequencies in current window
        char_count = {}
        char_count[s[left]] = 1

        while right < len(s):
            # Add right character to window
            char_count[s[right]] = char_count.get(s[right], 0) + 1

            # Current window length - count of most frequent char
            # represents the minimum changes needed
            while (right - left + 1) - max(char_count.values()) > k:
                # Window invalid: need more than k replacements
                char_count[s[left]] -= 1
                left += 1
            else:
                # Window valid: update max length and expand
                longest_sub = max(right - left + 1, longest_sub)
                right += 1

        return longest_sub

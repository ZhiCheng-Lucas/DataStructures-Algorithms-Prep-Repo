class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Problem: Check if s2 contains any permutation of s1 as a substring

        Solution approach:
        - Use sliding window technique with two hashmaps
        - One hashmap tracks character frequencies in s1
        - Another hashmap tracks character frequencies in current window of s2
        - Window size is fixed to length of s1
        - Compare hashmaps to check if current window is a permutation

        Time complexity: O(n) where n is length of s2
        Space complexity: O(k) where k is size of character set (26 lowercase letters)
        """

        # Return false if s1 is longer than s2, as no permutation possible
        if len(s1) > len(s2):
            return False

        # Create frequency map for pattern string s1
        pattern_freq = {}
        for char in s1:
            pattern_freq[char] = pattern_freq.get(char, 0) + 1

        # Initialize sliding window with first len(s1) characters of s2
        window_freq = {}
        left, right = 0, 0
        while right < len(s1):
            window_freq[s2[right]] = window_freq.get(s2[right], 0) + 1
            right += 1

        # right is pointing to the position AFTER the first window

        # Slide window through s2, checking for permutation match
        while right < len(s2):
            # Check if current window is a permutation
            if pattern_freq == window_freq:
                return True

            # Add new character to window
            window_freq[s2[right]] = window_freq.get(s2[right], 0) + 1

            # Remove leftmost character from window
            window_freq[s2[left]] -= 1
            if window_freq[s2[left]] == 0:
                del window_freq[s2[left]]

            left += 1
            right += 1

        # Check final window
        return pattern_freq == window_freq

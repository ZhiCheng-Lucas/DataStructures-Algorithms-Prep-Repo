class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Time Complexity: O(n) where n is the number of strings
        Space Complexity: O(1)
        """

        if not strs:
            return ""

        prefix = strs[0]

        for word in strs[1:]:
            i = 0

            # First position where string differs
            while i < len(prefix) and i < len(word) and prefix[i] == word[i]:
                i += 1

            prefix = prefix[:i]
        return prefix

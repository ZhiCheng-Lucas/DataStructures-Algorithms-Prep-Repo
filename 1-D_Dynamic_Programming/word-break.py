class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Word Break Problem - Dynamic Programming Solution

        The idea is to check if the string can be segmented into words from the dictionary.
        We use a DP array where dp[i] represents whether the substring s[0:i] can be segmented
        using words from wordDict.

        Strategy:
        - For each position i in string s, we check if any word from wordDict can end at i
        - If a word matches at position i, we check if the remaining prefix (dp[i-len(word)])
          was also segmentable
        - We use OR operation to handle multiple possible segmentation

        Time: O(n * m * k) where n = len(s), m = len(wordDict), k = average word length
        Space: O(n) for the dp array
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string is always segmentable

        # For each position in string
        for end in range(len(s) + 1):
            # Try each word from dictionary
            for word in wordDict:
                # Only check if current position can fit the word
                if end >= len(word):
                    # Extract substring of word length ending at current position
                    curr_substring = s[end - len(word) : end]
                    if curr_substring == word:
                        # Can segment if: current word matches AND
                        # remaining prefix (dp[end-len(word)]) was segmentable

                        # OR is required as override is possible
                        dp[end] = dp[end - len(word)] or dp[end]

        return dp[len(s)]

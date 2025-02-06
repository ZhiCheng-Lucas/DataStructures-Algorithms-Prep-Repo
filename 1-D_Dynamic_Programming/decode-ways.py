class Solution:
    def numDecodings(self, encoded_string: str) -> int:
        """
        A message encoded with numbers 1-26 (representing A-Z) needs to be decoded.
        We need to find the total number of possible decodings.

        Strategy:
        Using top-down dynamic programming with memoization:
        1. Start from the end of string and work backwards
        2. For each position, attempt to decode:
           - Single digit (if valid)
           - Two digits (if valid and within range 10-26)
        3. Cache results to avoid repeated computations

        Recurrence Relation:
        Let dp[i] = number of ways to decode substring s[0:i]

        dp[i] = dp[i-1] (if s[i-1] is valid single digit)
              + dp[i-2] (if s[i-2:i] is valid two-digit number)

        Breaking down the recurrence:
        1. dp[i-1] term:
           - A valid single digit means s[i-1] is not '0'
           - We can't decode '0' by itself since mappings start from '1' -> 'A'
           - Valid: '1' to '9' can be decoded to 'A' to 'I'
           - Invalid: '0' has no single-digit mapping

        2. dp[i-2] term:
           - A valid two-digit number means:
             a) First digit can't be '0' (no leading zeros)
             b) Number must be between 10 and 26 inclusive
           - Valid: "10" to "26" can be decoded to 'J' to 'Z'
           - Invalid: "00", "01", "27", "99", etc.

        3. Total ways at position i:
           - Sum of valid one-digit and two-digit decodings
           - Each term included only if its validity conditions are met

        Base Cases:
        - dp[0] = 1 (empty string)
        - dp[1] = 1 if s[0] != '0' else 0 (single character)

        Time: O(n) where n is string length
        Space: O(n) for memoization and recursion stack
        """
        # Dictionary to store previously computed results
        # Key: position in string being processed
        # Value: number of ways to decode substring from start to that position
        decoding_cache = {}

        def count_decodings(current_position: int) -> int:
            # Base case 1: Empty string has exactly one way to decode it
            if current_position == 0:
                return 1

            # Return previously computed result if available
            if current_position in decoding_cache:
                return decoding_cache[current_position]

            # Base case 2: Single character string
            # Can be decoded only if it's not '0'
            if current_position == 1:
                return 1 if encoded_string[0] != "0" else 0

            # Count total ways to decode string up to current position
            total_ways = 0

            # Try decoding single digit (must be 1-9)
            # Check if current digit is valid (not '0')
            current_digit = encoded_string[current_position - 1]
            if current_digit != "0":
                # Add ways to decode remaining string after using single digit
                total_ways += count_decodings(current_position - 1)

            # Try decoding two digits (must be 10-26)
            # Need at least 2 characters and value must be between 10 and 26
            if current_position > 1:
                two_digits = encoded_string[current_position - 2 : current_position]
                if "10" <= two_digits <= "26":
                    # Add ways to decode remaining string after using two digits
                    total_ways += count_decodings(current_position - 2)

            # Cache and return result for current position
            decoding_cache[current_position] = total_ways
            return total_ways

        # Start decoding from the end of string
        return count_decodings(len(encoded_string))

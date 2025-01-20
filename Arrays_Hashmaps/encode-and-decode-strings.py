class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings into a single string.

        Solution Approach:
        Use a length-based prefix system since a simple delimiter would be insufficient (delimiters could appear within the strings themselves).
        For each string, we prepend its length followed by a '#' delimiter:

        Example: ["neet", "code"] -> "4#neet4#code"
        - '4#' indicates the following string is 4 characters long
        - The '#' delimiter separates the length prefix from the actual string
        """
        encoded_string = ""
        for s in strs:
            count = len(s)
            prefix = str(count) + "#" + s
            encoded_string += prefix
        return encoded_string

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back into the original list of strings.

        The input string follows the format: <length>#<string><length>#<string>...
        Example: "4#neet4#code" decodes to ["neet", "code"]

        Note on string slicing in Python:
        string[start:end:step]
        - start: starting index (inclusive)
        - end: ending index (exclusive)
        - step: how many characters to skip

        The decoding process:
        1. Find the '#' delimiter
        2. Extract the length prefix before '#'
        3. Read exactly that many characters after '#'
        4. Repeat until the entire string is processed
        """
        result = []
        index = 0
        length = len(s)

        while index < length:
            # Locate the '#' delimiter
            delimiter_pos = index
            while s[delimiter_pos] != "#":
                delimiter_pos += 1

            # Extract the string length from the prefix
            str_length = int(s[index:delimiter_pos])  # Using string slicing to get length
            delimiter_pos += 1  # Move past '#'

            # Extract the string using the known length
            # Using string slicing: start at delimiter_pos, end at delimiter_pos + str_length
            current_string = s[delimiter_pos : delimiter_pos + str_length]
            result.append(current_string)

            # Move to the start of the next length prefix
            index = delimiter_pos + str_length

        return result

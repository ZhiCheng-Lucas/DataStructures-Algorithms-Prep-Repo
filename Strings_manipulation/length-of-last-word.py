class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        According to the docs. For split function,
        If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings


        If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator


        """

        # runs of consecutive whitespace are regarded as a single separator
        words = s.split()
        return len(words[-1])

        # res = 0
        # s = s.strip()
        # for i in s[::-1]:
        #     if i != " ":
        #         res +=1

        #     else:
        #         break
        # return res

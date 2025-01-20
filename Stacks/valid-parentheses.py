class Solution:
    """
    Valid Parentheses problem: checks if a string of brackets is properly nested.

    Solution:
    1. Stack: Tracks opening brackets to enforce proper nesting order
    2. HashMap: Maps opening brackets to their closing counterparts

    Example walkthrough:
    s = "([{}])"
    stack = []
    step 1: '(' → stack = ['(']
    step 2: '[' → stack = ['(', '[']
    step 3: '{' → stack = ['(', '[', '{']
    step 4: '}' → stack = ['(', '[']     # pop and match '{'
    step 5: ']' → stack = ['(']          # pop and match '['
    step 6: ')' → stack = []             # pop and match '('
    Empty stack → Valid!

    Time Complexity: O(n) - single pass through the string
    Space Complexity: O(n) - stack may store all opening brackets
    """

    def isValid(self, s: str) -> bool:
        bracket_pairs = {"(": ")", "{": "}", "[": "]"}
        stack = []

        for bracket in s:
            if bracket in bracket_pairs:
                # Current bracket is opening - add to stack
                stack.append(bracket)
            else:
                # Current bracket is closing - needs matching opening bracket
                if not stack or bracket_pairs[stack.pop()] != bracket:
                    return False

        # Valid only if all brackets were matched and closed
        return not stack

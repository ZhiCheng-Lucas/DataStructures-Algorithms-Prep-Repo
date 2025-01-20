class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluates an arithmetic expression in Reverse Polish Notation using a stack.

        The algorithm:
        1. Process tokens from left to right
        2. Push numbers onto stack
        3. When encountering an operator, pop two numbers and apply the operation
        4. Push result back to stack
        5. Final answer is the last number on stack

        Time Complexity: O(n) where n is length of tokens
        Space Complexity: O(n) in worst case for stack storage
        """
        stack = []

        # Define operations using lambda functions for cleaner evaluation
        # Note: eval() was avoided as it can execute arbitrary code

        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: int(x / y),  # Integer division with truncation
        }

        for token in tokens:
            # Case 1: Token is a positive number
            if token.isnumeric():
                stack.append(int(token))

            # Case 2: Token is a negative number
            elif token[0] == "-" and len(token) > 1:
                stack.append(int(token))

            # Case 3: Token is an operator
            else:
                second_value = stack.pop()
                first_value = stack.pop()

                # Calculate result and push back to stack
                result = operations[token](first_value, second_value)
                stack.append(result)

        # Final value on stack is the result of entire expression
        return stack.pop()

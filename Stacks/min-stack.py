class MinStack:
    """
    A stack implementation that supports constant time access to the minimum element.

    Solution:
    Use 2 stacks.
    1. Main stack: Stores all elements normally
    2. Min stack: Maintains the minimum value up to each position

    Example state:
    main_stack = [2, 1, 4, 5]
    min_stack  = [2, 1, 1, 1]

    Time Complexity: O(1) for all operations
    Space Complexity: O(n) where n is the number of elements in the stack

    Why two stacks?
    - Simply tracking the current minimum in a variable isn't sufficient
    - When we pop the minimum element, we need to know what the new minimum is
    - The min_stack ensures we always know the minimum for any state of the stack
    """

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if self.min_stack:
            current_min = self.min_stack[-1]
            # Propagate either the new value or existing minimum
            self.min_stack.append(min(current_min, val))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Approach : Monotonic Decreasing Stack

        We use a stack to keep track of temperatures and their indices. The stack maintains
        temperatures in decreasing order (larger temperatures at bottom, smaller at top).
        For each new temperature:
        - If it's warmer than temperatures in stack, we've found future warmer days for those entries
        - If it's colder, we add it to stack to find its warmer day later

        Example walkthrough with [73,74,75,71,69,72,76,73]:
        1. Start: stack=[[73,0]]
        2. See 74: 74>73, pop 73, calculate wait time: 1-0=1, stack=[[74,1]]
        3. See 75: 75>74, pop 74, calculate wait time: 2-1=1, stack=[[75,2]]
        4. See 71: 71<75, add to stack=[[75,2],[71,3]]
        5. Continue this process...

        Time: O(n) - each element is pushed and popped at most once
        Space: O(n) - in worst case (decreasing temperatures) all elements stay in stack
        """
        result_stack = [0] * len(temperatures)
        temp_stack = []  # stores [temperature, index] pairs

        for index, temp in enumerate(temperatures):
            # While we have temperatures in stack and found a warmer day
            while temp_stack and temp > temp_stack[-1][0]:
                prev_temp, prev_index = temp_stack.pop()
                result_stack[prev_index] = index - prev_index
            temp_stack.append([temp, index])

        return result_stack

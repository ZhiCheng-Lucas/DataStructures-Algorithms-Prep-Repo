class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Track the cumulative difference between gas and cost.
        - If total gas < total cost, it's impossible to complete the circuit
        - If a solution exists, it must be unique
        - When our running total becomes negative, we can skip all stations up to that point

        Strategy:
        1. First check if a solution is possible by comparing total gas to total cost
        2. Keep track of running total (gas[i] - cost[i]) and update potential starting position
        3. When running total goes negative, we know all positions up to current index cannot be the answer

        Time Complexity: O(n) - single pass through the arrays
        Space Complexity: O(1) - using only constant extra space
        """
        # Early return if total gas is less than total cost
        if sum(gas) - sum(cost) < 0:
            return -1

        running_total = 0
        start_station = 0

        for current_station in range(len(gas)):
            # Add the net gas (gain - cost) for current station
            running_total += gas[current_station] - cost[current_station]

            # If we run out of gas, start from the next station
            if running_total < 0:
                running_total = 0
                start_station = current_station + 1

        return start_station

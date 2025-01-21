class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Best Time to Buy and Sell Stock

        Strategy:
        Use two pointers to track potential buy and sell days. The left pointer
        represents the current minimum price (buy day), while the right pointer
        scans forward looking for the optimal sell day.

        For each position:
        - Calculate current profit using right (sell) - left (buy) prices
        - If right price is higher: continue scanning for potentially better sell price
        - If right price is lower: update buy position as we've found a new minimum

        Example:
        prices = [7,1,5,3,6,4]
        1. Start: buy at 7 (left)
        2. Find lower price 1: update buy position
        3. Scan remaining days keeping 1 as buy price
        4. Max profit = 6 - 1 = 5 (buy at 1, sell at 6)

        Time: O(n) - single pass through array
        Space: O(1) - only using two pointers and profit variable
        """

        max_profit = 0
        buy_day = 0  # Tracks day with minimum price seen so far
        sell_day = 1  # Scans forward looking for optimal sell day

        while sell_day < len(prices):
            current_profit = prices[sell_day] - prices[buy_day]
            max_profit = max(current_profit, max_profit)

            if prices[sell_day] >= prices[buy_day]:
                sell_day += 1  # Current buy day still optimal, check next sell day
            else:
                buy_day = sell_day  # Found new minimum price, update buy day
                sell_day += 1

        return max_profit

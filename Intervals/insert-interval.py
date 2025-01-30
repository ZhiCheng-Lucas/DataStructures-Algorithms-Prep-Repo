class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Insert and merge a new interval into a sorted list of non-overlapping intervals.

        Strategy:
        1. Process intervals one by one, comparing with newInterval:
           - If newInterval ends before current: insert and return early
           - If newInterval starts after current: keep current interval
           - If intervals overlap: merge them by updating bounds
        2. Any remaining merged interval is added at the end

        Time: O(n) where n is number of intervals
        Space: O(n) for the result list
        """
        res = []
        for i in range(len(intervals)):
            curr = intervals[i]
            # New interval comes before current - we can return immediately
            if newInterval[1] < curr[0]:
                res.append(newInterval)
                return res + intervals[i:]

            # Current interval comes before new interval - add it and continue
            elif newInterval[0] > curr[1]:
                res.append(curr)

            # Intervals overlap - merge them by updating newInterval's bounds
            else:
                newInterval = (min(curr[0], newInterval[0]), max(curr[1], newInterval[1]))

        # Add final merged interval
        res.append(newInterval)
        return res

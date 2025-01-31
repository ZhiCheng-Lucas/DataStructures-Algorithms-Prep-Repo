class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges overlapping intervals by first sorting them by start time and then
        combining intervals that overlap.

        Strategy:
        1. Sort intervals by start time to ensure sequential processing
        2. Use two pointers to compare adjacent intervals
        3. If intervals overlap, merge them by taking:
           - minimum of both start times
           - maximum of both end times
        4. If no overlap, add the left interval to result

        Time complexity: O(nlogn) - sorting step
        Space complexity: O(n) - result list
        """

        # Handle single interval case
        if len(intervals) == 1:
            return intervals

        # Sort by start time to ensure overlapping intervals are adjacent
        intervals.sort(key=lambda interval: interval[0])

        res = []
        left, right = 0, 1  # Two pointers for comparing adjacent intervals

        while right < len(intervals):
            # Two intervals overlap if:
            # end time of first interval >= start time of second interval
            # AND end time of second interval >= start time of first interval
            current_overlaps = intervals[left][1] >= intervals[right][0] and intervals[right][1] >= intervals[left][0]

            if current_overlaps:
                # Merge by taking min start time and max end time
                intervals[right] = [
                    min(intervals[right][0], intervals[left][0]),
                    max(intervals[right][1], intervals[left][1]),
                ]
            else:
                # No overlap - add left interval to result
                res.append(intervals[left])

            left += 1
            right += 1

        # Add the last interval
        res.append(intervals[left])
        return res

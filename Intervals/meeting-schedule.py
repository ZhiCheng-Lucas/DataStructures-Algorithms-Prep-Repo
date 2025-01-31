"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Meeting Rooms - Interval Overlap Check

        Determine if all meetings can be scheduled without any time conflicts.
        Two meetings conflict if one meeting starts before another meeting ends.

        Strategy:
        - Sort meetings by start time to check adjacent intervals efficiently
        - For any two meetings to not overlap, one meeting must end before the next begins
        - Edge case: Meetings that end exactly when another begins (e.g., (1,5) and (5,8)) are valid

        Time complexity: O(nlogn) - sorting operation
        Space complexity: O(1) - Only using pointers, original array is modified in place
        """

        # Sort meetings by start time to ensure we compare meetings chronologically
        intervals.sort(key=lambda interval: interval.start)

        # Use two pointers to compare adjacent meetings
        curr, next_meeting = 0, 1
        while next_meeting < len(intervals):
            # A conflict occurs if:
            # 1. Current meeting ends after next meeting starts AND
            # 2. Next meeting ends after current meeting starts
            if (
                intervals[next_meeting].end > intervals[curr].start
                and intervals[curr].end > intervals[next_meeting].start
            ):
                return False

            curr += 1
            next_meeting += 1

        return True

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)

        for i in range(len(intervals) - 1, 0, -1):
            if intervals[i-1].start < intervals[i].start < intervals[i-1].end or intervals[i-1].start < intervals[i].end < intervals[i-1].end or (intervals[i-1].start == intervals[i].start and intervals[i-1].end == intervals[i].end) or intervals[i].start < intervals[i-1].start < intervals[i].end or intervals[i].start < intervals[i-1].end < intervals[i].end:
                return False
        return True

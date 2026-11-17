class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        n = len(intervals)
        result = [intervals[-1]]
        print(intervals)
        for i in range(n-2, -1, -1):
            if result[0][0] < intervals[i][0] < result[0][1] or intervals[i][0] < result[0][0] < intervals[i][1] or (result[0] == intervals[i]) or result[0][0] < intervals[i][1] < result[0][1] or intervals[i][0] < result[0][1] < intervals[i][1] :
                pass
            else:
                result = [intervals[i]] + result
        print(result)
        return len(intervals) - len(result)


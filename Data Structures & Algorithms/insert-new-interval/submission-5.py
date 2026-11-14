class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        result = []
        n = len(intervals)

        for i in range(n):
            if intervals[i][0] > newInterval[1]:
                result.append(newInterval)
                return result + intervals[i:]
            elif intervals[i][0] <= newInterval[0] <= intervals[i][1] or  newInterval[0] <= intervals[i][0] <= newInterval[1]:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1],newInterval[1])]
            else:
                result.append(intervals[i])
        result.append(newInterval)
        return result
            

            

            


        
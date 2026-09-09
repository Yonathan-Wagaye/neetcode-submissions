import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        heapq.heapify(intervals)
        result = []
        while len(intervals) > 1:
            first = heapq.heappop(intervals)
            second =intervals[0]
            if first[0] <= second[0] <= first[1]:
                first[1] = max(first[1], second[1])
                heapq.heappop(intervals)
                heapq.heappush(intervals, first)
            else:
                result.append(first)
        if intervals: result.append(heapq.heappop(intervals))

        return result
            
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x,y in points:
            heapq.heappush(heap, (x**2 + y**2, [x,y]))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        return result
        
            
        
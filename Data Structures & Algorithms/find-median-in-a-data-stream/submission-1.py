import heapq

class MedianFinder:

    def __init__(self):
        self.large = [] # min heap
        self.small = [] # max heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, num * -1)
        if self.large and self.large[0] < -self.small[0]:
            smallRoot = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * smallRoot)
        if len(self.small) - len(self.large) > 1:
            smallRoot = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, smallRoot)
        if len(self.large) - len(self.small) > 1:
            largeRoot = heapq.heappop(self.large)
            heapq.heappush(self.small, largeRoot * -1)

    def findMedian(self) -> float:
        if len(self.large) == len(self.small):
            return ((self.large[0]) + -self.small[0]) / 2
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return -self.small[0]
        
        
        
        
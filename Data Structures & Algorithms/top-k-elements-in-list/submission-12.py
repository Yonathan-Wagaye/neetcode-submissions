class PriorityQueue:
    def __init__(self):
        self.heap = [None]
        self.pMap = {}

    @classmethod
    def mapToHeap(cls, priorityMap):
        heap = cls()
        heap.pMap = priorityMap
        heap.heap = heap.heap + list(heap.pMap.keys())
        heap._heapify()
        return heap

    def _percolateDown(self, nodeIndex):
        curr = nodeIndex
        n = len(self.heap) - 1
        
        while curr < n:
            children = self._getChildren(curr)
            hasLeft, hasRight, leftChild, rightChild = (
                children[0][0],
                children[0][1],
                children[1][0],
                children[1][1],
            )
            if hasLeft and hasRight:  # has left and right child
                if self._greaterThan(
                    leftChild, rightChild, equal=True
                ) and self._greaterThan(
                    leftChild, curr
                ):  # left child the correct root of subtree
                    self.heap[curr], self.heap[leftChild] = (
                        self.heap[leftChild],
                        self.heap[curr],
                    )
                    curr = leftChild

                elif self._greaterThan(rightChild, leftChild) and self._greaterThan(
                    rightChild, curr
                ):  # right child the correct root of subtree
                    self.heap[curr], self.heap[rightChild] = (
                        self.heap[rightChild],
                        self.heap[curr],
                    )
                    curr = rightChild

                else: # current node correct root of subtree
                    break

            elif hasLeft and self._greaterThan(leftChild, curr): # has left child only
                    self.heap[curr], self.heap[leftChild] = (
                        self.heap[leftChild],
                        self.heap[curr],
                    )
                    curr = leftChild
              

            elif hasRight and self._greaterThan(rightChild, curr): # has right child only
                    self.heap[curr], self.heap[rightChild] = (
                        self.heap[rightChild],
                        self.heap[curr],
                    )
                    curr = rightChild

            else: # correct positon
                break
              
            

    def _heapify(self):
        n = len(self.heap) - 1
        curr = n // 2
        while curr > 0:
            self._percolateDown(curr)
            curr -= 1

    def _lessThan(
        self, nodeOne, nodeTwo, equal=False
    ):  # nodeOne < nodeTwo or nodeOne <= nodeTwo
        if equal:
            return self.pMap[self.heap[nodeOne]] <= self.pMap[self.heap[nodeTwo]]
        else:
            return self.pMap[self.heap[nodeOne]] < self.pMap[self.heap[nodeTwo]]

    def _greaterThan(
        self, nodeOne, nodeTwo, equal=False
    ):  # nodeOne > nodeTwo or nodeOne >= nodeTwo
        if equal:
            return self.pMap[self.heap[nodeOne]] >= self.pMap[self.heap[nodeTwo]]
        else:
            return self.pMap[self.heap[nodeOne]] > self.pMap[self.heap[nodeTwo]]

    def _getChildren(self, nodeIndex):
        leftChild = 2 * nodeIndex
        rightChild = leftChild + 1
        n = len(self.heap)
        children = [[False, False], [leftChild, rightChild]]
        if 0 < leftChild < n:
            children[0][0] = True
        if 0 < rightChild < n:
            children[0][1] = True
        return children

    def pop(self):
        if len(self.heap) == 1:
            return None
        root = self.heap[1]
        self.heap[1] = self.heap[-1]
        self.heap.pop()
        self._percolateDown(1)
        return root




class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []

        hashMap = {}
        
        for num in nums:
            if num not in hashMap: hashMap[num] = 1
            else: hashMap[num] += 1
        
        pQueue = PriorityQueue.mapToHeap(hashMap)
        return [pQueue.pop() for _ in range(k)]        

        


        
        
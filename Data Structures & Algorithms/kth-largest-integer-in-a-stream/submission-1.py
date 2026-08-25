class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = [-1]
        self.k = k

        for num in nums:
            self.add(num) 


    def add(self, val: int) -> int:
        n = len(self.minHeap) - 1

        if n < self.k:
            self.minHeap.append(val)
            i = n+1

            while i > 1:
                if self.minHeap[i//2] > self.minHeap[i]:
                    self.minHeap[i//2], self.minHeap[i] = self.minHeap[i], self.minHeap[i//2]
                    i //= 2
                else:
                    break
        else:
            if val > self.minHeap[1]:
                self.minHeap[1] = val
                i = 1
                end = self.k + 1
                leftChild = 2 * i
                rightChild = 2 * i + 1

                while leftChild < end:
                    if  rightChild < end:
                        if self.minHeap[leftChild] < self.minHeap[i] and self.minHeap[rightChild] >= self.minHeap[leftChild]:

                            self.minHeap[i], self.minHeap[leftChild] = self.minHeap[leftChild], self.minHeap[i]
                            i = leftChild
                        
                        elif self.minHeap[rightChild] < self.minHeap[i] and self.minHeap[leftChild] > self.minHeap[rightChild]:
                            self.minHeap[i], self.minHeap[rightChild] = self.minHeap[rightChild], self.minHeap[i]
                            i = rightChild

                        else:break

                    else:
                        if self.minHeap[i] > self.minHeap[leftChild]:
                            self.minHeap[i], self.minHeap[leftChild] = self.minHeap[leftChild], self.minHeap[i]
                            i = leftChild
                        else: break
                            
                    leftChild = 2 * i
                    rightChild = 2 * i + 1     
        return self.minHeap[1]     
        
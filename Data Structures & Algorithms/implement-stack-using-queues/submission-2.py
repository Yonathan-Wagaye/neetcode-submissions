class Queue:

    def __init__(self):
        self.array = []
        self.size = 0

    def pushToBack(self, x: int) -> None:
        self.array.append(x)
        self.size += 1
    
    def popFromFront(self) -> int:
        if not self.isEmpty():
            self.size -= 1
            return self.array.pop(0)
        return -1

    def size(self) -> int:
        return self.size

    def isEmpty(self) -> bool:
        return self.size == 0

class MyStack:

    def __init__(self):
        self.queueOne = Queue()
        self.queueTwo = Queue()

    def push(self, x: int) -> None:
        if not self.queueOne.isEmpty():
            self.queueOne.pushToBack(x)
        else:
            self.queueTwo.pushToBack(x)
        
    def pop(self) -> int:
        if self.queueTwo.isEmpty():
            for _ in range(self.queueOne.size - 1):
                self.queueTwo.pushToBack(self.queueOne.popFromFront())
            return self.queueOne.popFromFront()
        else:
            for _ in range(self.queueTwo.size - 1):
                self.queueOne.pushToBack(self.queueTwo.popFromFront())
            return self.queueTwo.popFromFront()
        
        
    def top(self) -> int:
        if self.queueTwo.isEmpty():
            for _ in range(self.queueOne.size - 1):
                self.queueTwo.pushToBack(self.queueOne.popFromFront())
            lastElem = self.queueOne.popFromFront()
            self.queueTwo.pushToBack(lastElem)
            return lastElem
        else:
            for _ in range(self.queueTwo.size - 1):
                self.queueOne.pushToBack(self.queueTwo.popFromFront())
            lastElem = self.queueTwo.popFromFront()
            self.queueOne.pushToBack(lastElem)
            return lastElem

    def empty(self) -> bool:
        return self.queueTwo.isEmpty() and self.queueOne.isEmpty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
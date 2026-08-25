class Node:
    def __init__(self, val=None):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.length = 0
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, index: int) -> int:
        currentNode = self.head.next
        counter = 0
        while currentNode.next:
            if counter == index:
                return currentNode.val
            counter += 1
            currentNode = currentNode.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        headNext = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = headNext
        headNext.prev = newNode
        self.length += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        tailPrev = self.tail.prev
        self.tail.prev = newNode
        newNode.next = self.tail
        newNode.prev = tailPrev
        tailPrev.next = newNode
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.length:
            self.addAtTail(val)

        else:
            currentNode = self.head.next
            counter = 0
            while currentNode.next:
                if counter == index:
                    newNode = Node(val)
                    currentPrev = currentNode.prev
                    newNode.next = currentNode
                    newNode.prev = currentPrev
                    currentNode.prev = newNode
                    currentPrev.next = newNode
                    self.length += 1
                    break
                currentNode = currentNode.next
                counter += 1
            
        

    def deleteAtIndex(self, index: int) -> None:
        currentNode = self.head.next
        counter = 0
        while currentNode.next:
            if counter == index:
                currentPrev = currentNode.prev
                currentNext = currentNode.next
                currentNext.prev = currentPrev
                currentPrev.next = currentNext
                self.length -= 1
                break
            currentNode = currentNode.next
            counter += 1

    
    
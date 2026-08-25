class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def addBack(self, val):
        newNode = Node(val)
        lastNode = self.tail.prev
        lastNode.next = newNode
        newNode.prev = lastNode
        newNode.next = self.tail
        self.tail.prev = newNode

        return newNode

    def removeFront(self):
        if self.head.next != self.tail:
            front = self.head.next
            self.head.next = front.next
            front.next.prev = self.head
            front.next = None
            front.prev = None
            return front.val

    def removeNode(self, node):
        nextNode = node.next
        prevNode = node.prev

        prevNode.next = nextNode
        nextNode.prev = prevNode

        node.next = None
        node.prev = None






class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key: (value, )
        self.lru_list = DoublyLinkedList()
        self.currentCapacity = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.cache:
            keyNode = self.cache[key][1]
            self.lru_list.removeNode(keyNode)
            self.cache[key][1] = self.lru_list.addBack(key)
            return self.cache[key][0]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if self.capacity > self.currentCapacity:
                self.cache[key] = [value, self.lru_list.addBack(key)]
                self.currentCapacity += 1
            else:
                leastUsed = self.lru_list.removeFront()
                self.cache.pop(leastUsed)
                self.cache[key] = [value, self.lru_list.addBack(key)]
        else:
            keyNode = self.cache[key][1]
            self.lru_list.removeNode(keyNode)
            self.cache[key] = [value, self.lru_list.addBack(key)]
            

            
                
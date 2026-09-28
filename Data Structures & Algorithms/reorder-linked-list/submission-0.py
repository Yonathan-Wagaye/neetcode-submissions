# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        current = head
        n = 0
        while current:
            stack.append(current)
            current = current.next
            n += 1

        currentNode = head
        nextNode = currentNode.next
        for _ in range(n//2):
            top = stack.pop()
            currentNode.next = top
            top.next = nextNode

            currentNode = nextNode
            nextNode = nextNode.next
        
        currentNode.next = None
          

        
        

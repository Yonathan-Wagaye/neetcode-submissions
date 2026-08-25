# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        else:
            prev = head
            current = prev.next
            while current != None:
                next = current.next
                current.next = prev
                prev = current
                current = next
            head.next = None          
            return prev
        
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        current = head
        while current:
            N += 1
         
            current = current.next
        
        if N > n:
            prev = head
            for _ in range(N-n - 1):
                prev= prev.next
        
   
            removed = prev.next
            if removed:
                prev.next = removed.next
            else:
                head = removed
        else:
            head = head.next
        return head

            

        
        
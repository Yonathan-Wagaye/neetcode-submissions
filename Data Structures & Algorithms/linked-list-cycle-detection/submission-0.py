# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        prevMap = {}
        index = -1
        current = head
        i = 0
        while current != None and index == -1:
            if current.next in prevMap:
                index = i
            else:
                prevMap[current.next] = current
            current = current.next
            i += 1
        return index != -1
        
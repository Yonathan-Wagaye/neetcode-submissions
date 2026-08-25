# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def merge(self, list1: ListNode, list2: ListNode):
        if not list1:
            return list2
        elif not list2:
            return list1
        else:
            dummy = ListNode()
            dummy.next = list1
            p1 = dummy
            c1 = list1
            c2 = list2
            while c1 and c2:
                if c1.val >= c2.val:
                    temp = c2.next
                    c2.next = c1
                    p1.next = c2
                    p1 = c2
                    c2 = temp
                else:
                    p1 = c1
                    c1 = c1.next
            if c2:
                p1.next = c2
            return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        newNode = lists[0]
        for i in range(1, n):
            newNode = self.merge(newNode, lists[i])
        return newNode
           
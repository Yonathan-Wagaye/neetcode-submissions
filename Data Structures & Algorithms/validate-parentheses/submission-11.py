from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        hashMap = {'(': ')', '{': '}', '[' : ']'}


        for p in s:
            if p in hashMap:
                stack.appendleft(p)
            elif stack:
                if p != hashMap[stack.popleft()]: return False
            else: return False

        return len(stack) == 0

        
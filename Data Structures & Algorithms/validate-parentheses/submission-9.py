class Solution:
    def isValid(self, s: str) -> bool:
        compatability = ['[]', '()', '{}']
        stack = []
        n = len(s)
        for i in range(n):
            if stack and stack[-1] + s[i] in compatability:
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack) == 0
        
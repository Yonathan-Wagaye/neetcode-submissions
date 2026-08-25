from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseToReq = {i:[] for i in range(numCourses)}
        for course, preq in prerequisites:
            courseToReq[course].append(preq)

        sortedCourses = []
        callStack = deque([])
        print(courseToReq)

        def dfs(course):
            if course in callStack:
                return False
            callStack.append(course)
            if course in sortedCourses:
                callStack.pop()
                return True
            
            reqs = courseToReq[course]
            for preq in reqs:
                if not dfs(preq):
                    callStack.pop()
                    return False
            sortedCourses.append(course)
            callStack.pop()
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        print(sortedCourses)
        return True
        
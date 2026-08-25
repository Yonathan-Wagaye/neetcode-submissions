class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = {0: students.count(0), 1: students.count(1)}
        n = len(sandwiches)

        for i in range(n):
            if count[sandwiches[i]] == 0:
                break
            count[sandwiches[i]] -= 1
            
        return count[0] + count[1]
            


        
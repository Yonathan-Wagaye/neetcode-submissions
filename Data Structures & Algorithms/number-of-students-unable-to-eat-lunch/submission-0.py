class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        
        while n > 0:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                n = len(students)
            else:
                firstStudent = students.pop(0)
                students.append(firstStudent)
                n -= 1

        return len(students)

        
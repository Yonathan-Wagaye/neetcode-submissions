class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        startBucket = [-1] * 1001
        for start,end in intervals:
            startBucket[start] = max(startBucket[start], end)

        result = []
        for i in range(1001):
            if startBucket[i] != -1:
                if result and result[-1][0] <= i <= result[-1][1]:
                    result[-1][1] = max(startBucket[i], result[-1][1])
                else:
                    result.append([i, startBucket[i]])
        return result 


        


        
        
        
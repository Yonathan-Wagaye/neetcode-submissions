class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(i):
            count = 0 
            while i > 0: 
                if i & 1 == 1:
                    count += 1
                i = i >> 1
            return count

        result = []
        for i in range(n+1):
            result.append(count(i))
        return result

        
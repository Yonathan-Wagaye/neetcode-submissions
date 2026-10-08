class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        curr = []
        
        def dfs(i):
            if i > n + 1 or len(curr) > k:
                return
            if len(curr) == k:
                result.append(curr.copy())
                return
            
            # with i
            curr.append(i)
            dfs(i+1)

            #without i
            curr.pop()
            if k - len(curr) > n - i: return   
            dfs(i+1)

            return
        dfs(1)

        return result
        
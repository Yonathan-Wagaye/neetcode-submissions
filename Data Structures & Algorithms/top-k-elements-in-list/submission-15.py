class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num not in hashMap: hashMap[num] = 1
            else: hashMap[num] += 1

        maxFreq = max(list(hashMap.values()))
        bucket = [[] for _ in range(maxFreq+1)]

   

        for num in hashMap:
            bucket[hashMap[num]].append(num)

        print(bucket)
        result = []
        n = len(bucket) - 1
        
        while n >= 0:
            print(n)
            currentBucket = bucket[n]
            i = len(currentBucket) - 1
            while i >= 0 and k > 0:
                result.append(currentBucket[i])
                i -= 1
                k -= 1
            n -= 1
        return result
         
        
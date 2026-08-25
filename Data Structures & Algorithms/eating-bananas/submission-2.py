from math import ceil

class Solution:
    def isRateValid(self, piles: List[int], h: int, k: int) -> bool:
        possibleTotalToEat = k * h
        totalToEat = sum(piles)
        if possibleTotalToEat < totalToEat: return False
        initalHour = h
        print("Inital hour= ", h)

        n = len(piles)
        for i in range(n):
            h -= ceil(piles[i] / k)
            if h >= 0 :
                piles[i] = 0
            else:
                break
            

            
        print(f"After checking validity of k={k}, piles={piles} totalHoursTake={initalHour - h}")
        return piles[-1] == 0
             
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        possibleMinK = -1

        while start <= end:
            mid = (start + end) // 2
            if self.isRateValid([*piles], h, mid):
                possibleMinK = mid
                end = mid - 1
            else:
                start = mid + 1
        return possibleMinK
         

        
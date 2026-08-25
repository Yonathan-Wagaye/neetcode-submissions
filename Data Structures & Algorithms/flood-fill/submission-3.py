class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        n, m = len(image), len(image[0])
       
        

        def dfsFill(sr, sc):
            # check bounds 
            if sr < 0 or sc < 0 or sr >= n or sc >= m:
                return image
            
            currentColor = image[sr][sc]

             # already colored
            if image[sr][sc] == color:
                return image 

            # check obstacle
            if startingColor != currentColor:
                return image

            image[sr][sc] = color
            
            dfsFill(sr + 1, sc)
            dfsFill(sr - 1, sc)
            dfsFill(sr, sc + 1)
            dfsFill(sr, sc - 1)

            return image
        dfsFill(sr, sc)
        return image
            
        
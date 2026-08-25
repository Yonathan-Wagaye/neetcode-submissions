class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]
        n, m = len(image), len(image[0])
        # already colored
        if image[sr][sc] == color:
            return image 

        def dfsFill(sr, sc):
            

            # check bounds 
            if sr < 0 or sc < 0 or sr >= n or sc >= m:
                return image
            
            currentColor = image[sr][sc]

            

            # check obstacle
            if startingColor != currentColor:
                return image

            image[sr][sc] = color
            
            dfsFill(sr + 1, sc)
            dfsFill(sr - 1, sc)
            dfsFill(sr, sc + 1)
            dfsFill(sr, sc - 1)

            return image
        return dfsFill(sr, sc)
            
        
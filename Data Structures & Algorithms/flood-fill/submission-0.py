class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startingColor = image[sr][sc]

        def dfsFill(image, sr, sc, color, startingColor):
            n, m = len(image), len(image[0])

            # check bounds 
            if sr < 0 or sc < 0 or sr >= n or sc >= m:
                return image
            
            currentColor = image[sr][sc]

            # already colored
            if currentColor == color:
                return image 

            # check obstacle
            if startingColor != currentColor:
                return image

            image[sr][sc] = color
            
            dfsFill(image, sr + 1, sc, color, startingColor)
            dfsFill(image, sr - 1, sc, color, startingColor)
            dfsFill(image, sr, sc + 1, color, startingColor)
            dfsFill(image, sr, sc - 1, color, startingColor)

            return image
        return dfsFill(image, sr, sc, color, startingColor)
            
        
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        currentColor = image[sr][sc]

        def floodFillHelper(sr, sc):
            if 0<=sr<len(image) and 0<=sc<len(image[0]) and image[sr][sc] == currentColor and image[sr][sc] != color:
                image[sr][sc] = color
                floodFillHelper(sr-1, sc)
                floodFillHelper(sr, sc-1)
                floodFillHelper(sr+1, sc)
                floodFillHelper(sr, sc+1)
        
        floodFillHelper(sr,sc)

        return image
        
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        check = image[sr][sc]
        if check == color:
            return image
        
        m = len(image[0])
        n = len(image)

        def fill(sr, sc):
            if sr >= n or sc >= m or sr < 0 or sc < 0:
                return

            if image[sr][sc] == check:
                image[sr][sc] = color
            
                fill(sr,sc+1)
                fill(sr,sc-1)
                fill(sr+1,sc)
                fill(sr-1,sc)
            return image

        return fill(sr, sc)

        


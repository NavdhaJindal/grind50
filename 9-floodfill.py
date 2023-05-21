class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if (sr < len(image) and sc < len(image[0])):
            original_color = image[sr][sc]
            image[sr][sc] = color
            print(sr, sc)

            if (sr + 1 < len(image) and image[sr+1][sc] == original_color):
                print("down from ", sr, sc)
                self.floodFill(image, sr + 1, sc, color)
            if (sr - 1 >= 0 and image[sr-1][sc] == original_color):
                print("up from from ", sr, sc)
                self.floodFill(image, sr - 1, sc, color)
            if (sc + 1 < len(image[0]) and image[sr][sc + 1] == original_color):
                print("right from ", sr, sc)
                self.floodFill(image, sr, sc + 1, color)
            if (sc - 1 >= 0 and image[sr][sc-1]  == original_color):
                print("left from ", sr, sc)
                self.floodFill(image, sr, sc - 1, color)
        
        print("returning from ", sr, sc)
        print(image)
        return image
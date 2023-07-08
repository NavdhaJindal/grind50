class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # original_col = image[sr][sc]
        # if original_col == color:
        #     return image
        
        # def dfs(r: int, c: int) -> None:
        #     if r >= len(image) or r < 0 or c >= len(image[0]) or c < 0 or image[r][c] != original_col: 
        #         return
        #     image[r][c] = color

        #     dfs(r + 1, c)
        #     dfs(r - 1, c)
        #     dfs(r, c + 1)
        #     dfs(r, c - 1)

        #     return

        # dfs(sr, sc)

        # return image

        stack = [(sr, sc)]
        pixelsCovered = {}
        original_color = image[sr][sc]
        while stack:
            sr, sc = stack.pop()
            if pixelsCovered.get((sr, sc), False) == False:
                if image[sr][sc] == original_color:
                    image[sr][sc] = color
                    pixelsCovered[sr, sc] = True

                    if (sr + 1 < len(image) and image[sr+1][sc] == original_color):
                        stack.append((sr + 1, sc))

                    if (sr - 1 >= 0 and image[sr-1][sc] == original_color):
                        stack.append((sr - 1, sc))

                    if (sc + 1 < len(image[0]) and image[sr][sc + 1] == original_color):
                        stack.append((sr, sc + 1))

                    if (sc - 1 >= 0 and image[sr][sc-1]  == original_color):
                        stack.append((sr, sc - 1))
        return image




# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         if (sr < len(image) and sc < len(image[0])):
#             original_color = image[sr][sc]
#             image[sr][sc] = color
#             print(sr, sc)

#             if (sr + 1 < len(image) and image[sr+1][sc] == original_color):
#                 print("down from ", sr, sc)
#                 self.floodFill(image, sr + 1, sc, color)
#             if (sr - 1 >= 0 and image[sr-1][sc] == original_color):
#                 print("up from from ", sr, sc)
#                 self.floodFill(image, sr - 1, sc, color)
#             if (sc + 1 < len(image[0]) and image[sr][sc + 1] == original_color):
#                 print("right from ", sr, sc)
#                 self.floodFill(image, sr, sc + 1, color)
#             if (sc - 1 >= 0 and image[sr][sc-1]  == original_color):
#                 print("left from ", sr, sc)
#                 self.floodFill(image, sr, sc - 1, color)
        
#         print("returning from ", sr, sc)
#         print(image)
#         return image
# class Solution(object):
#     def floodFill(self, image, sr, sc, color):
#         """
#         :type image: List[List[int]]
#         :type sr: int
#         :type sc: int
#         :type color: int
#         :rtype: List[List[int]]
#         """

#         m = len(image)
#         n = len(image[0])

#         original = image[sr][sc]

       
#         if original == color:
#             return image

#         stack = [(sr, sc)]
#         visited = set()
#         visited.add((sr, sc))

#         while stack:
#             i, j = stack.pop()

#             image[i][j] = color

#             directions = [
#                 (1, 0),
#                 (-1, 0),
#                 (0, 1),
#                 (0, -1)
#             ]

#             for dx, dy in directions:

#                 x = i + dx
#                 y = j + dy

#                 if (0 <= x < m and
#                     0 <= y < n and
#                     (x, y) not in visited and
#                     image[x][y] == original):

#                     visited.add((x, y))
#                     stack.append((x, y))

#         return image



class Solution(object):
    def floodFill(self, image, sr, sc, color):

        m = len(image)
        n = len(image[0])

        original = image[sr][sc]

        if original == color:
            return image

        stack = [(sr, sc)]

        while stack:

            i, j = stack.pop()

            if image[i][j] != original:
                continue

            image[i][j] = color

            if i > 0:
                stack.append((i - 1, j))

            if i < m - 1:
                stack.append((i + 1, j))

            if j > 0:
                stack.append((i, j - 1))

            if j < n - 1:
                stack.append((i, j + 1))

        return image
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        visited = set()

        def dfs(i, j, org):
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]) or image[i][j] != org:
                return

            if (i, j) in visited:
                return

            visited.add((i, j))

            image[i][j] = color

            dfs(i + 1, j, org)
            dfs(i - 1, j, org)
            dfs(i, j + 1, org)
            dfs(i, j - 1, org)
        
        dfs(sr, sc, image[sr][sc])
        return image
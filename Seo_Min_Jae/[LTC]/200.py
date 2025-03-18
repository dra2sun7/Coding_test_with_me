class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return False
            
            if grid[x][y] == "1":
                grid[x][y] = "0"

                dfs(x-1, y)
                dfs(x+1, y)
                dfs(x, y-1)
                dfs(x, y+1)

                return True
            
            return False

        m = len(grid)
        n = len(grid[0])

        count = 0

        for i in range(m):
            for j in range(n):
                if dfs(i, j) == True:
                    count += 1
        
        return count
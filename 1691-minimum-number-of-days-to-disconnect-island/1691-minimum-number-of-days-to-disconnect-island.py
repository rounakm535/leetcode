class Solution(object):
    def minDays(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return
            grid[i][j] = 2  # Mark as visited
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(i + di, j + dj)
        
        def count_islands():
            count = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        dfs(i, j)
                        count += 1
            # Reset grid
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 2:
                        grid[i][j] = 1
            return count
        
        # Check if already disconnected
        if count_islands() != 1:
            return 0
        
        # Check if removing any single land cell disconnects the island
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        
        # If not, we need 2 days
        return 2
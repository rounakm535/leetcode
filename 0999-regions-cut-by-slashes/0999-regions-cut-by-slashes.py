class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        n = len(grid)
        parent = list(range(4 * n * n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for i in range(n):
            for j in range(n):
                if i > 0:
                    union(4 * (i * n + j), 4 * ((i - 1) * n + j) + 2)
                if j > 0:
                    union(4 * (i * n + j) + 3, 4 * (i * n + j - 1) + 1)
                
                if grid[i][j] != '/':
                    union(4 * (i * n + j), 4 * (i * n + j) + 1)
                    union(4 * (i * n + j) + 2, 4 * (i * n + j) + 3)
                if grid[i][j] != '\\':
                    union(4 * (i * n + j), 4 * (i * n + j) + 3)
                    union(4 * (i * n + j) + 1, 4 * (i * n + j) + 2)
        
        return len(set(find(x) for x in range(4 * n * n)))
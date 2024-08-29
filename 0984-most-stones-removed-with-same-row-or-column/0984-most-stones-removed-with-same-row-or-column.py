class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
                return 1
            return 0
        
        n = len(stones)
        parent = list(range(20001))  # Assuming max coordinate is 10^4
        
        row_map = {}
        col_map = {}
        components = n
        
        for i, (x, y) in enumerate(stones):
            if x not in row_map:
                row_map[x] = i
            if y + 10001 not in col_map:  # Offset column by 10001 to avoid collision with row
                col_map[y + 10001] = i
            
            components -= union(i, row_map[x])
            components -= union(i, col_map[y + 10001])
        
        return n - components
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def is_magic_square(sub_grid):
            # Check if all numbers are distinct and between 1 and 9
            flat = [num for row in sub_grid for num in row]
            if set(flat) != set(range(1, 10)):
                return False
            
            # Check row sums
            target_sum = sum(sub_grid[0])
            if any(sum(row) != target_sum for row in sub_grid):
                return False
            
            # Check column sums
            if any(sum(col) != target_sum for col in zip(*sub_grid)):
                return False
            
            # Check diagonal sums
            if sum(sub_grid[i][i] for i in range(3)) != target_sum:
                return False
            if sum(sub_grid[i][2-i] for i in range(3)) != target_sum:
                return False
            
            return True

        count = 0
        rows, cols = len(grid), len(grid[0])
        
        for i in range(rows - 2):
            for j in range(cols - 2):
                sub_grid = [grid[i+k][j:j+3] for k in range(3)]
                if is_magic_square(sub_grid):
                    count += 1
        
        return count
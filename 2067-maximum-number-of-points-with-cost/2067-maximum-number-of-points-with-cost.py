class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m, n = len(points), len(points[0])
        
        # Initialize the previous row
        prev = points[0]
        
        for i in range(1, m):
            curr = [0] * n
            
            # Left to right
            left_max = 0
            for j in range(n):
                left_max = max(left_max - 1, prev[j])
                curr[j] = left_max + points[i][j]
            
            # Right to left
            right_max = 0
            for j in range(n - 1, -1, -1):
                right_max = max(right_max - 1, prev[j])
                curr[j] = max(curr[j], right_max + points[i][j])
            
            prev = curr
        
        return max(prev)
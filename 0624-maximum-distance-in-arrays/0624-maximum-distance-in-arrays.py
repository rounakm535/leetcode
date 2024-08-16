class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        max_dist = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        
        for i in range(1, len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]
            
            max_dist = max(max_dist, 
                           abs(curr_max - min_val), 
                           abs(max_val - curr_min))
            
            min_val = min(min_val, curr_min)
            max_val = max(max_val, curr_max)
        
        return max_dist
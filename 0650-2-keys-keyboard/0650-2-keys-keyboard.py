class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        
        dp = [0] * (n + 1)
        
        for i in range(2, n + 1):
            dp[i] = i  # Worst case: copy 'A' and paste i-1 times
            
            # Check for factors
            for j in range(i - 1, 1, -1):
                if i % j == 0:
                    dp[i] = dp[j] + (i // j)
                    break
        
        return dp[n]
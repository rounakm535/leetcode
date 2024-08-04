class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        # Generate all subarray sums
        all_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                all_sums.append(current_sum)
        
        # Sort the sums
        all_sums.sort()
        
        # Calculate the range sum
        result = sum(all_sums[left-1:right])
        
        # Return the result modulo 10^9 + 7
        return result % (10**9 + 7)
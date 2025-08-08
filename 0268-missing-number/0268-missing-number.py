from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  
        total = 0
        arr_sum = 0

        i = 0
        while i <= n:
            total += i
            i += 1

        for num in nums:
            arr_sum += num

        miss = total - arr_sum
        return miss

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:

        total_chalk = sum(chalk)
        
        k %= total_chalk
        
        for i, chalk_needed in enumerate(chalk):
            if k < chalk_needed:
                return i
            k -= chalk_needed
        
        return -1
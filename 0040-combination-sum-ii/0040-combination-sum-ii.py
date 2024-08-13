class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                
                path.append(candidates[i])
                backtrack(i + 1, target - candidates[i], path)
                path.pop()
        
        candidates.sort()  # Sort to handle duplicates and optimize
        result = []
        backtrack(0, target, [])
        return result

# Test the solution
sol = Solution()

# Example 1
candidates1 = [10,1,2,7,6,1,5]
target1 = 8
print(sol.combinationSum2(candidates1, target1))

# Example 2
candidates2 = [2,5,2,1,2]
target2 = 5
print(sol.combinationSum2(candidates2, target2))
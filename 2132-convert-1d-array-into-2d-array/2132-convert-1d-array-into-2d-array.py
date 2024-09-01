class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        # Check if it's possible to create an m x n 2D array
        if len(original) != m * n:
            return []
        
        # Initialize the 2D array
        result = []
        
        # Iterate through the original array
        for i in range(0, len(original), n):
            # Slice the original array to create each row
            row = original[i:i+n]
            result.append(row)
        
        return result
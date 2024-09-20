class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        # Create the new string with reverse for KMP processing
        rev_s = s[::-1]
        combined = s + '#' + rev_s
        
        # Build KMP table (partial match table)
        kmp = [0] * len(combined)
        
        for i in range(1, len(combined)):
            j = kmp[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = kmp[j - 1]
            if combined[i] == combined[j]:
                j += 1
            kmp[i] = j
        
        # The length of the longest palindromic prefix
        longest_palindrome_len = kmp[-1]
        
        # Find the characters to add to the front
        non_palindrome_suffix = s[longest_palindrome_len:]
        
        # Return the shortest palindrome by prepending the reverse of the non-palindromic suffix
        return non_palindrome_suffix[::-1] + s
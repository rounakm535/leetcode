from fractions import Fraction

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        # Add '+' to the beginning if the expression doesn't start with a sign
        if expression[0] not in ['+', '-']:
            expression = '+' + expression
        
        # Split the expression into individual fractions
        fractions = []
        i = 0
        while i < len(expression):
            if expression[i] in ['+', '-']:
                sign = expression[i]
                j = i + 1
                while j < len(expression) and expression[j] not in ['+', '-']:
                    j += 1
                fractions.append(sign + expression[i+1:j])
                i = j
            else:
                i += 1
        
        # Calculate the sum of fractions
        result = sum(Fraction(f) for f in fractions)
        
        # Convert the result to string format
        return "{0}/{1}".format(result.numerator, result.denominator)

# Test the solution
sol = Solution()
print(sol.fractionAddition("-1/2+1/2"))  # Output: "0/1"
print(sol.fractionAddition("-1/2+1/2+1/3"))  # Output: "1/3"
print(sol.fractionAddition("1/3-1/2"))  # Output: "-1/6"
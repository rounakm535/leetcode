class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Find the number of bits in num
        bit_length = num.bit_length()
        
        # Create a mask with all 1's of the same length as num
        mask = (1 << bit_length) - 1
        
        # XOR num with the mask to flip all bits
        return num ^ mask
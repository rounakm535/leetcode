"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # Recursive solution
        def recursive_postorder(node):
            if not node:
                return []
            
            result = []
            for child in node.children:
                result.extend(recursive_postorder(child))
            result.append(node.val)
            
            return result
        
        # Iterative solution
        def iterative_postorder(root):
            if not root:
                return []
            
            stack = [root]
            result = []
            
            while stack:
                node = stack.pop()
                result.append(node.val)
                stack.extend(node.children)
            
            return result[::-1]
        
        # Uncomment the solution you want to use
        # return recursive_postorder(root)
        return iterative_postorder(root)
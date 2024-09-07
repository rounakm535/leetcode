class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, head: ListNode) -> bool:
            if not head:
                return True
            if not node or node.val != head.val:
                return False
            return dfs(node.left, head.next) or dfs(node.right, head.next)

        def traverse(node: TreeNode) -> bool:
            if not node:
                return False
            if dfs(node, head):
                return True
            return traverse(node.left) or traverse(node.right)

        return traverse(root)
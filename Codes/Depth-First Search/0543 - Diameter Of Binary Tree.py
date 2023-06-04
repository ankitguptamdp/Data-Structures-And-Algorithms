# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = [0] # Global Variable

        def DFS(root):
            if not root:
                return -1

            left = DFS(root.left)
            right = DFS(root.right)
            result[0] = max(result[0], left + right + 2)

            return max(left, right) + 1

        DFS(root)
        return result[0]
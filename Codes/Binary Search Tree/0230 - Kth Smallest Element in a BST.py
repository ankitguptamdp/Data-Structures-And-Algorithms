# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sortedArray = []

        def DFS(root):
            if not root:
                return None

            DFS(root.left)
            sortedArray.append(root.val)
            DFS(root.right)

            return sortedArray

        DFS(root)
        return sortedArray[k-1]
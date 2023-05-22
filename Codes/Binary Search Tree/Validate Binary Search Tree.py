# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root: Optional[TreeNode], output):
        if root == None:
            return
        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)
        return output

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        outputArray = []
        outputArray = self.inorder(root, outputArray)
        for index in range(len(outputArray)-1):
            if outputArray[index] >= outputArray[index+1]:
                return False
        return True
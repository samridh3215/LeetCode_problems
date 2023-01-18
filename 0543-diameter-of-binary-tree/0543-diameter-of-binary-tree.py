# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDiameter(self, root):
        if (root ==None):
            return 0
        left = self.getDiameter(root.left)
        right = self.getDiameter(root.right)
        d = left+right
        self.mDia = max(self.mDia, d)
        return max(left, right)+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mDia = 0
        self.getDiameter(root)
        return self.mDia
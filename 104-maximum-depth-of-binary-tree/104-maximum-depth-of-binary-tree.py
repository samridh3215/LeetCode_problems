# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        NULL = None
        def findHeight(root, depth):
            if(root==NULL):
                return depth
            left = findHeight(root.left, depth+1)
            right = findHeight(root.right, depth+1)
            return max(left, right)
        ans = findHeight(root, depth)
        return ans
            
            
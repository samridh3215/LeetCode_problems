# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(root):

            if root == None:
                return 0
            return 1+max(check(root.left), check(root.right))
        if not root:
            return True
        else:
            res = abs(check(root.left)-check(root.right))
            return (res<2 and self.isBalanced(root.left) and self.isBalanced(root.right))
        
        
        
        
        
        
        # def checkLeft(root):
        #     if root == None:
        #         return 1
        #     else:
        #         return 1+checkLeft(root.left)
        # def checkRight(root):
        #     if root == None:
        #         return 1
        #     else:
        #         return 1+checkRight(root.right)
        # if abs(checkLeft(root)-checkRight(root)) >1:
        #     return 0
        # return 1

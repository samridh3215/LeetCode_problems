# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = TreeNode(val)
        b= root
        if not root:
            return node
    
        while b:
            if val < b.val:
                if b.left is None:
                    b.left = node
                    break
                else:
                    b = b.left
            else:
                if b.right is None:
                    b.right = node
                    break
                else:
                    b= b.right
        
        return root
            
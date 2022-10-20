# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else: # delete the root
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            prev = root
            nex = root.right
            while nex and nex.left:
                prev = nex
                nex = nex.left
            
            root.val = nex.val
            if prev == root:
                prev.right = nex.right
            else:
                prev.left = nex.right
        return root
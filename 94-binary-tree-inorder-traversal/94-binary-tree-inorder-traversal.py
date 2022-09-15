# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []
        self.inorder(root, nodes)
        return nodes
        
    def inorder(self, root: Optional[TreeNode], nodes: List[int]) -> List[int]:
        if root is not None:
            self.inorder(root.left, nodes)
            nodes.append(root.val)
            self.inorder(root.right, nodes)
        
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None: return ""
        s = str(root.val)
        if root.left:
            s+= f"({self.tree2str(root.left)})"
        if root.left==None and root.right:
            s+= "()"
        if root.right:
            s+= f"({self.tree2str(root.right)})"
        return s
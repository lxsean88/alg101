def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root or (not root.left and not root.right):
        return root
    left = invertTree(root.right)
    right = invertTree(root.left)
    root.left = left
    root.right = right
    return root


    ans = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def height(root):
            if not root:
                return 0
            left = height(root.left)
            right = height(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
        height(root)
        return self.ans

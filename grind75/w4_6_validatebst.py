
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValidHelper(root: Optional[TreeNode], minvalue: int, maxvalue: int) -> bool:
            if not root:
                return True
            if root.val > maxvalue or root.val < minvalue:
                return False

            return isValidHelper(root.left, minvalue, root.val - 1) & isValidHelper(root.right, root.val + 1, maxvalue)

        return isValidHelper(root, -sys.maxsize, sys.maxsize)

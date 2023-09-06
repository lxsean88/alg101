
def height(root) -> int:
    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    
    left = height(root.left)
    if left == -1:
        return -1

    right = height(root.right)
    if right == -1 or left - right > 1 or right - left > 1:
        return -1

    return max(left, right) + 1
    
def isBalanced(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    left = height(root.left)
    if left == -1:
        return False

    right = height(root.right)
    if right == -1 or left - right > 1 or right - left > 1:
        return False

    return True

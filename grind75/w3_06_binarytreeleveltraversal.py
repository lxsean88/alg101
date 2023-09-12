
dev levelOrder(root: Optional(Treenode)) -> List[List[int]]:
    rst = []
    if not root:
        return rst
    que = deque()
    que.append(root)

    while que:
        n = len(que)
        cur= []
        for _ in range(n):
            node = que.popleft()
            cur.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        rst.append(cur)

    return rst

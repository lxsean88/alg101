    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        que = deque()
        que.append(root)
        rst = []
        while que:
            n = len(que)
            for i in range(n):
                node = que.popleft()
                if i == n-1:
                    rst.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        
        return rst

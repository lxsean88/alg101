
def cloneGraph(node):
    if not node:
        return

    visited = {}
    visited[node] = Node(node.val)
    que = deque()
    que.append(node)
    while que:
        n = que.popleft()
        for neighbor in n.neighbours:
            if not neighbor in visited:
                visited[neighbor] = Node(neighbor.val)
                que.append(neighbor)
            visited[n].neighbors.append(visited[neighbor])
    return visited[node]

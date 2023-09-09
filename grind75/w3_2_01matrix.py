
def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    rst = [ [0]*n for _ in range(m) ]
    zeros = [(i, j) for i in range(m) for j in range(n) if mat[m][n] == 0]
    visited = set(zeros)
    que = deque(zeros)

    def isvalid(x, y):
        if 0<=x<m and 0<=y<n and not (x, y) in visited:
            return True
        return False

    dx = [1, -1, 0, 0]
    dy = [-1, 1, 0, 0]
    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[j]
            if isvalid(nx, ny):
                rst[nx][ny] = rst[cx][cy] + 1
                que.append((nx, ny))
                visited.add((nx, ny))
    return rst


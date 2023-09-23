class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isvalid(x, y):
            if not (0<=x<len(grid) and 0<=y<len(grid[0])):
                return False
            return True

        if not grid or not grid[0]:
            return -1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        mins = -1
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        que = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append((i, j))
                    visited[i][j] = 1
        
        while que:
            n = len(que)
            mins += 1
            for _ in range(n):
                x, y = que.popleft()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if isvalid(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
                        grid[nx][ny] = 2
                        visited[nx][ny] = 1
                        que.append((nx, ny))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        
        if mins < 0:
            mins = 0
        return mins 


        

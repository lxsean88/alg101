class Solution:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        if not grid or not grid[0]:
            return islands
        
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        return islands   

    def bfs(self, grid, x, y, visited):
            que = deque([(x, y)])
            visited.add((x, y))
            while que:
                x, y = que.popleft()
                for dx, dy in self.directions:
                    nx, ny = x+dx, y+dy
                    if self.isvalid(grid, nx, ny, visited):
                        que.append((nx, ny))
                        visited.add((nx, ny))

    
    def isvalid(self, grid, x, y, visited):
        if not (0 <= x < len(grid) and 0 <= y < len(grid[0])):
            return False
        
        if (x, y) in visited:
            return False

        return grid[x][y]

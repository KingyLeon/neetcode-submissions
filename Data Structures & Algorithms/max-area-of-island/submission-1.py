class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))

            area = 1
            while q:
                row, col = q.popleft()
                DIRS = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in DIRS:
                    nr, nc = row + dr, col + dc
                    if (nr in range(rows) and 
                    nc in range(cols) and 
                    grid[nr][nc] == 1 and
                    (nr,nc) not in visited):
                        visited.add((nr, nc))
                        q.append((nr,nc))
                        area += 1
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea
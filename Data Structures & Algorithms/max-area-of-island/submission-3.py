class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        msum = 0

        def dfs(r, c):
            if r >= row or r < 0 or c >= col or c < 0:
                return 0
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            
            d = dfs(r + 1, c)
            u = dfs(r - 1, c)
            ri = dfs(r, c + 1)
            l = dfs(r, c - 1)

            return 1 + d + u + ri + l
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    s = dfs(r, c)
                    msum = max(msum, s)
        return msum
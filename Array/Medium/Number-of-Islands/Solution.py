class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through grid
        # if grid is unvisited land
        # explore entire island recursively
        # add 1 to island count
        # mark grid as visited (2) as you land there

        ROWS = len(grid)
        COLS = len(grid[0])
        islandCount = 0

        def explore(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return
            if grid[r][c] != '1':
                return
            
            grid[r][c] = '2'
            explore(r + 1, c)
            explore(r - 1, c)
            explore(r, c + 1)
            explore(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    explore(r, c)
                    islandCount += 1
        
        return islandCount
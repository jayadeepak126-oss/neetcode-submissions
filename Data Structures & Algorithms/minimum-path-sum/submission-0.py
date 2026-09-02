class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        row, col = len(grid), len(grid[0])
        dp = dp = [float("inf")] * (col + 1)
        dp[col - 1] = 0

        for r in range(row -1, -1, -1):
            for c in range(col - 1, -1, -1):
                dp[c] = grid[r][c] + min(dp[c], dp[c+1])
        
        return dp[0]
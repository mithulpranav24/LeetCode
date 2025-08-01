from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] < 0:
                    c+=1
        return c
        print(m,n)

print(Solution().countNegatives([[1,0],[0,1],[-1,0],[0,-1]]))

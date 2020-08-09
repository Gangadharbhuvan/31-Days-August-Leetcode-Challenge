'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.


'''

from collections import deque

class Solution:
    def is_cell_valid(self, cell_i, cell_j):
        return (cell_i >= 0 and cell_i <= self.n - 1) and (cell_j >= 0 and cell_j <= self.m -1)
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        n, m = len(grid), len(grid[0])
        seen_fresh = 0
        longest_time = 0
        self.n, self.m = n,m
        
        # Seeding queue and fresh counter
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    
                elif grid[i][j] == 1:
                    seen_fresh += 1
            
        neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while q:
            cell_i, cell_j, time = q.popleft()
    
            if grid[cell_i][cell_j] == 1:
                seen_fresh -= 1    
                grid[cell_i][cell_j] = 2
                longest_time = max(longest_time, time)
            
            for nei_i, nei_j in neighbors:
                new_i, new_j = cell_i + nei_i, cell_j + nei_j
                
                if self.is_cell_valid(new_i, new_j) and grid[new_i][new_j] == 1:
                    q.append((new_i, new_j, time + 1))
                
        return longest_time if not seen_fresh else -1
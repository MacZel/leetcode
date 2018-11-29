class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)
        x_projection_area = sum([max(towers_row) for towers_row in grid])
        z_projection_area = 0
        y_projection = [0]*N
        for towers_row in grid:
            for i in range(N):
                if towers_row[i] > 0:
                    z_projection_area += 1
                if towers_row[i] > y_projection[i]:
                    y_projection[i] = towers_row[i]
        y_projection_area = sum(y_projection)
        
        total_area = x_projection_area + y_projection_area + z_projection_area
        return total_area
class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxRows = [max(row) for row in grid]
        # maxCols = []
        # for col_i in range(len(grid)):
        #     maxCol = []
        #     for row in grid:
        #         maxCol.append(row[col_i])
        #     maxCols.append(maxCol)
        maxCols = [max([row[col_i] for row in grid]) for col_i in range(len(grid))]
        height_diff = 0
        
        for row_i in range(len(grid)):
            for col_i in range(len(grid)):
                max_height = min([maxRows[row_i], maxCols[col_i]])
                curr_building_height = grid[row_i][col_i]
                if curr_building_height < max_height:
                    height_diff += max_height - curr_building_height
        return height_diff

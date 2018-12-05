/**
 * @param {number[][]} grid
 * @return {number}
 */
const maxIncreaseKeepingSkyline = grid => {
    let N = grid.length
    let maxRows = Array(N)
    let maxCols = Array(N)
    maxRows.fill(0)
    maxCols.fill(0)
    
    for (let i=0; i<N; i++) {
        for (let j=0; j<N; j++) {
            if (grid[i][j] > maxRows[i]) {
                maxRows[i] = grid[i][j]
            }
            if (grid[j][i] > maxCols[i]) {
                maxCols[i] = grid[j][i]
            }
        }
    }
    
    let height_diff = 0;
    for (let i=0; i<N; i++) {
        for (let j=0; j<N; j++) {
            let max_height = Math.min(maxRows[i], maxCols[j])
            let curr_building_height = grid[i][j]
            if (curr_building_height < max_height) {
                height_diff += max_height - curr_building_height
            }  
        }
    }
    return height_diff
}
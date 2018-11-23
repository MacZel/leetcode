/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
const rotate = matrix => {
    let N = matrix.length
    
    for (let i=0; i < Math.floor(N/2); i++) {
        
        for (let j=i; j < N-i-1; j++) {
            let copy_curr = matrix[i][j]
            let copy_next = 0
            
            for (let k=0; k < 4; k++) {
                let t = i
                i = j
                j = N-t-1
                copy_next = matrix[i][j]
                matrix[i][j] = copy_curr
                copy_curr = copy_next
            }
        }
    }
    return
}
/**
 * @param {number[][]} A
 * @return {number[][]}
 */
const transpose = A => {
    let N_rows = A.length
    let N_cols = A[0].length
    // If A is a square matrix, transpose in place
    if (N_rows == N_cols) {
        for (let row_i=0; row_i<N_rows; row_i++) {
            for (let col_i=row_i+1; col_i<N_rows; col_i++) {
                let temp = A[row_i][col_i]
                A[row_i][col_i] = A[col_i][row_i]
                A[col_i][row_i] = temp
            };
        }
        return A
    }
    // otherwise create new matrix
    else {
        let A_T = []
        for (let col_i=0; col_i<N_cols; col_i++) {
            let row_T = []
            for (let row_i=0; row_i<N_rows; row_i++) {
                row_T.push(A[row_i][col_i])
            }
            A_T.push(row_T)
        }
        return A_T
    }
}
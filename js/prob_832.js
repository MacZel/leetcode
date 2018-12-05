/**
 * @param {number[][]} A
 * @return {number[][]}
 */
const flipAndInvertImage = A => {
    let N = A.length
    for (let i=0; i<N; i++) {
        A[i] = A[i].reverse()
        for (let j=0; j<N; j++) {
            A[i][j] = A[i][j] == 0 ? 1 : 0
        }
    }
    return A
}
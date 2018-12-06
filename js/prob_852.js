/**
 * @param {number[]} A
 * @return {number}
 */
const peakIndexInMountainArray = A => {
    let curr_max = 0
    let curr_peak = 0
    for (let i=0; i<A.length; i++) {
        if (A[i] > curr_max) {
            curr_max = A[i]
            curr_peak = i
        }
    }
    return curr_peak
}
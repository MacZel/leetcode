/**
 * @param {string} s
 * @return {number}
 */
const lengthOfLongestSubstring = s => {
    let n = s.length
    let chartable = Array(128).fill(0)
    let ans = 0
    
    for (let i=0, j=0; j<n; j++) {
        i = Math.max(chartable[s.charCodeAt(j)], i)
        ans = Math.max(ans, j-i+1)
        chartable[s.charCodeAt(j)] = j+1
    }
    
    return ans
}

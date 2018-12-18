/**
 * @param {string} s
 * @param {number} numRows
 * @return {string}
 */
const convert = (s, numRows) => {
    if (numRows > 1) {
        let wordMatrix = []
        
        while (s) {
            let vertical = s.slice(0, numRows)
            let diagonal = s.slice(numRows, 2*(numRows-1))
                            .split("").reverse().join("")
            diagonal = " ".repeat(numRows - diagonal.length - 1).concat(diagonal)
            vertical ? wordMatrix.push(vertical) : null
            vertical ? wordMatrix.push(diagonal) : null
            s = s.slice(2*(numRows-1))
        }
        let ans = ""
        for (let row_i=0; row_i < numRows; row_i++) {
            for (let word of wordMatrix) {
                ans = ans.concat(word.slice(row_i, row_i+1))
            }
        }
        ans = ans.replace(/ /g, "")
        return ans
    }
    else {
        return s
    }
}
/**
 * @param {number} num
 * @return {string}
 */
const intToRoman = num => {
    const INT2ROMAN = [
        ['I', 'V'],
        ['X', 'L'],
        ['C', 'D'],
        ['M']
    ]
    let ans = ''
    for (let i=0; i<4; i++) {
        let digit = parseInt(num % 10)
        num /= 10
        let pre = ''
        
        if (digit < 4) {
            pre = INT2ROMAN[i][0].repeat(digit)
        }
        else if (digit == 4) {
            pre = INT2ROMAN[i][0] + INT2ROMAN[i][1]
        }
        else if (digit < 9) {
            pre = INT2ROMAN[i][1] + INT2ROMAN[i][0].repeat(digit % 5)
        }
        else {
            pre = INT2ROMAN[i][0] + INT2ROMAN[i+1][0]
        }
        ans = pre + ans
    }
    return ans 
}
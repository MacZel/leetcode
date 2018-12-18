/**
 * @param {string} str
 * @return {number}
 */
const myAtoi = str => {
    const LIMIT = 2147483648 // 2**31
    const INT_MIN = -LIMIT
    const INT_MAX = LIMIT -1
    
    let temp_str = str.trimLeft()
    let ans = 0
    let signmap = {
        43: 1,
        45: -1
    }
    let sign = 1
    
    let curr_char = null
    if (temp_str) {
        curr_char = temp_str[0].charCodeAt(0)
        if ([43, 45].includes(curr_char)) {
            sign = signmap[curr_char]
            temp_str = temp_str.slice(1)
        }
    }

    while (temp_str && curr_char !== 32) {
        curr_char = temp_str[0].charCodeAt(0)
        if (curr_char >= 48 && curr_char <= 57) {
            ans *= 10
            ans += parseInt(temp_str[0])
            temp_str = temp_str.slice(1)
        }
        else {
            break
        }
    }
    ans *= sign
    
    if (ans < INT_MIN) {
        return INT_MIN
    }
    else if (ans > INT_MAX) {
        return INT_MAX
    }
    else {
        return ans
    }
}
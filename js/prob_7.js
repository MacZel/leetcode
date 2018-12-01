/**
 * @param {number} x
 * @return {number}
 */
const reverse = x => {
    let neg = x < 0 ? -1 : 1
    x = Math.abs(x)
    
    let ans = 0
    while (x != 0) {
        ans = ans * 10 + x % 10
        x = parseInt(x / 10)
    }
    
    ans *= neg
    
    lim = Math.pow(2, 31)
    if (ans >= -lim && ans <= lim-1) {
        return ans
    }
    else {
        return 0
    }
}
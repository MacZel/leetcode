/**
 * @param {string} s
 * @return {number}
 */
const romanToInt = s => {
    const ROMAN2INT = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    let ans = 0
    for (let i=0; i<s.length; i++) {
        let sign = 1
        if (i != s.length - 1 && ROMAN2INT[s[i]] < ROMAN2INT[s[i+1]]) {
            sign = -1
        }
        ans += sign * ROMAN2INT[s[i]]
    }
    return ans
}
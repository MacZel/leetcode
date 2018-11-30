/**
 * @param {number} x
 * @return {boolean}
 */
const isPalindrome = x => {
    let copy_x = x
	
	if (x < 0) {
		return false
	}
	else {
		let reversed_x = 0
		while (x != 0) {
			reversed_x = reversed_x * 10 + x % 10
			x = parseInt(x / 10)
		}
		if (copy_x == reversed_x) {
			return true
		}
		else {
			return false
		}
	}
}
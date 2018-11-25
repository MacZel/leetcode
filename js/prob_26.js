/**
 * @param {number[]} nums
 * @return {number}
 */
const removeDuplicates = nums => {
    !nums && 0
    
    let carret = 0
    for (let i=1; i < nums.length; i++) {
        if (nums[carret] != nums[i]) {
            carret++
            nums[carret] = nums[i]
        }
    }
    return carret+1
};
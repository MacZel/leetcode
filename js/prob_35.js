/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
const searchInsert = (nums, target) => {
    let target_index = 0
        for (let i=0; i<nums.length; i++) {
            if (target > nums[i]) {
                target_index++
            }
        }
    return target_index
}
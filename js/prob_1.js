/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
const twoSum = (nums, target) => {
    let num_obj = {}
    for (let i=0; i < nums.length; i++) {
        num_obj[nums[i]] = i
    }
    
    let res = []
    for (let i=0; i < nums.length; i++) {
        let result = target - nums[i]
        
        if (result in num_obj && num_obj[result] != i) {
            res.push(i, num_obj[result])
            
            return res
        }
    }
    return res
}

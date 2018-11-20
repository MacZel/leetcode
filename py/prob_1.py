class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {num:i for i, num in enumerate(nums)}
        res = []
        
        for i in range(len(nums)):
            result = target - nums[i]
            if result in num_map and num_map[result] != i:
                res.extend([i, num_map[result]])
                
                return res    
        return res

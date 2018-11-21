class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        carret = 0
        for i in range(1, len(nums)):
            if nums[carret] != nums[i]:
                carret += 1
                nums[carret] = nums[i]
        
        return carret + 1
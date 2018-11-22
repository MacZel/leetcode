class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        target_index = 0
        for index in range(len(nums)):
            if target > nums[index]:
                target_index += 1
        return target_index

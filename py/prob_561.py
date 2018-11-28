class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        sum_mins = 0
        for pair in range(int(len(nums)/2)):
            sum_mins += nums[pair*2]
        return sum_mins
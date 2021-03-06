class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n_nums = len(nums)
        res = []
        for i in range(n_nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            goal = -nums[i]
            start, end = i+1, n_nums-1
            while start < end:
                if nums[start] + nums[end] == goal:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                elif nums[start] + nums[end] < goal:
                    start += 1
                else:
                    end -= 1
        return res

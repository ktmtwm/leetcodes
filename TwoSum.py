class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            left = target - nums[i]
            if left in nums and nums.index(left) != i:
                return i, nums.index(left)
        return 'Cannot find index sum!'
        
               

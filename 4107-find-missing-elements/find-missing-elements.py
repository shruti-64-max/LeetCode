class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        min=nums[0]
        max=nums[0]
        ans=[]
        for i in range(len(nums)):
            if nums[i]<min:
                min=nums[i]
            if nums[i]>max:
                max=nums[i]
        for i in range(min,max+1):
            if i not in nums:
                ans.append(i)
        return ans

        
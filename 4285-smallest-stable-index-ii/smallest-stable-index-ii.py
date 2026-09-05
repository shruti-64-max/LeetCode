class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        mini=[0]*n
        mini[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            mini[i]=min(nums[i],mini[i+1])
        maxi=nums[0]
        for i in range(n):
            maxi=max(nums[i],maxi)
            if maxi-mini[i]<=k:
                return i
        return -1

        
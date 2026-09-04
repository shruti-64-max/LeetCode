class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            maxi=max(nums[0:i+1])
            mini=min(nums[i:n])
            if maxi-mini<=k:
                return i
        return -1
        
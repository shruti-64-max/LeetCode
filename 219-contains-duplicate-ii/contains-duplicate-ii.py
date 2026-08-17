class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        grps={}
        for i in range(len(nums)):
            if nums[i] in grps:
                values=grps[nums[i]]
                dist=abs(i-values)

                if dist<=k:
                    return True
            grps[nums[i]]=i
        return False
            
        
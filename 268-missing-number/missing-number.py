class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while nums:
            if i not in nums:
                return i
            i+=1
            

        
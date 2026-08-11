class Solution(object):
    def removeDuplicates(self, nums):
        expectedNums=[]
        k=0
        
        for i in nums:
            if i in expectedNums:
                continue
            else:
                expectedNums.append(i)
                k+=1
        
        for i in range(k):
            nums[i]=expectedNums[i]
            
        return k
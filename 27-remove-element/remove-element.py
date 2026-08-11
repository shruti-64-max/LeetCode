class Solution(object):
    def removeElement(self, nums, val):
        k=0
        expectedNums=[]
        for i in nums:
            if i==val:
                continue
            else:
                expectedNums.append(i)
                k+=1
        for i in range(k):
            nums[i]=expectedNums[i]
        return k
        
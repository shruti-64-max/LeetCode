class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=""
        for i in range(32):
                ans+=str(n%2)
                n=n//2
        
        ans1=0
        for ch in ans:
            ans1=ans1*2+int(ch)

        return ans1
        
        
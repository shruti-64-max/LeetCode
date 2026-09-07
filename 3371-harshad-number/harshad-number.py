class Solution(object):
    def sumOfTheDigitsOfHarshadNumber(self, x):
        """
        :type x: int
        :rtype: int
        """
        num=x
        sum=0
        while num>0:
            dig=num%10
            sum+=dig
            num=num//10
        if x%sum==0:
            return sum
        else:
            return -1
        
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        seen2={}
        for i in magazine:
            seen2[i]=seen2.get(i,0)+1
        for i in ransomNote:
            if i not in seen2 or seen2[i]==0:
                return False
            seen2[i]-=1
        return True


                
        
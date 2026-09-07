class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            return False
        v="AEIOUaeiou"
        isv=False
        isc=False
        for ch in word:
            if not ch.isalnum():
                return False
            if ch in v:
                isv=True
            elif ch.isalpha():
                isc=True
        return isv and isc

            
        
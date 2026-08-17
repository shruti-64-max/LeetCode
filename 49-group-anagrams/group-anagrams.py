class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        grps={}
        for i in strs:
            keys="".join(sorted(i))
            if keys not in grps:
                grps[keys]=[]

            grps[keys].append(i)
        return list(grps.values())


            
        
        
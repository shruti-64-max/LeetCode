class Solution(object):
    def canMakeSquare(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        for i in range(2):
            for j in range(2):
                b=0
                w=0
                for x in range(i,i+2):
                    for y in range(j,j+2):
                        if grid[x][y]=="B":
                            b+=1
                        else:
                            w+=1
                if b>=3 or w>=3:
                    return True
        return False


        
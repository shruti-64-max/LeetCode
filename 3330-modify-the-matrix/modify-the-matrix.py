class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        row=len(matrix)
        col=len(matrix[0])
        for j in range(col):
            maxi=0
            for i in range(row):
                maxi=max(maxi,matrix[i][j])
            for i in range(row):
                if matrix[i][j]==-1:
                    matrix[i][j]=maxi
        return matrix
                


        
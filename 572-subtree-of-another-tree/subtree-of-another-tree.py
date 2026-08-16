# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool

        """
        def sametree(root,subroot):
            if root is None and subroot is None:
                return True
            if root is None or subroot is None:
                return False
            if root.val!=subroot.val:
                return False
            return sametree(root.left,subroot.left) and sametree(root.right, subroot.right)
        if root is None:
            return False
        if sametree(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        
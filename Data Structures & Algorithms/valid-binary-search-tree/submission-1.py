# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(cur, min, max):
            if not cur:
                return True
            if not (min<cur.val<max):
                return False
            return (isValid(cur.left, min, cur.val) and isValid(cur.right, cur.val, max))

        return isValid(root, float('-inf'), float('inf'))
            


        

        
        
            
        
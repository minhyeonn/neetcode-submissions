# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(cur, cur_greatest):
            nonlocal res
            if not cur:
                return
            if cur.val>=cur_greatest:
                res+=1
                cur_greatest = cur.val

            dfs(cur.left, cur_greatest)
            dfs(cur.right, cur_greatest)



        
        dfs(root, root.val)
        return res


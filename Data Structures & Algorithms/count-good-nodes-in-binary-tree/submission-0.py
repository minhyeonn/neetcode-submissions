# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(cur, max_val):
            if not cur:
                return 0
            
            good_node = 1 if cur.val>=max_val else 0

            new_max = max(cur.val, max_val)

            return good_node + dfs(cur.left, new_max) + dfs(cur.right, new_max)
            


        return dfs(root, root.val)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, cur_greatest):

            if not node:
                return 0
            if node.val>=cur_greatest:
                good = 1
            else:
                good = 0
            cur_greatest = max(cur_greatest, node.val)

            
            return good + dfs(node.left, cur_greatest) + dfs(node.right, cur_greatest)
        return dfs(root, root.val)


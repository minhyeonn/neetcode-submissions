# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(cur):
            if not cur:
                return [0, True]
            left = dfs(cur.left)
            right = dfs(cur.right)
            diff = abs(right[0] - left[0])
            
            balanced = diff<2 and left[1] and right[1]

            return [1+max(left[0], right[0]), balanced]

        return dfs(root)[1]
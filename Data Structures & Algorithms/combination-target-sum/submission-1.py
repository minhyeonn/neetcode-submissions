class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sum_list = []
        def dfs(i, cur_sum):
            if cur_sum==target:
                res.append(sum_list.copy())
                return
            if i>=len(nums) or cur_sum>target:
                return
            
            sum_list.append(nums[i])
            dfs(i, cur_sum+nums[i])
            sum_list.pop()
            dfs(i+1, cur_sum)

        dfs(0, 0)
        return res
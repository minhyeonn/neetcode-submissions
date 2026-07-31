class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sum_list = []
        def dfs(i , cur_sum):
            if cur_sum==target:
                res.append(sum_list.copy())
                return

            if i>=len(candidates)or cur_sum>target:
                return

            sum_list.append(candidates[i])
            dfs(i+1, cur_sum+candidates[i])
            sum_list.pop()
            while i+1 < len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1, cur_sum)
        dfs(0,0)
        return res
